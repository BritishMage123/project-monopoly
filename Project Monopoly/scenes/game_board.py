from scenes.scene import Scene
from ui.button import Button
from entities.dice import Dice
from entities.game_agent import GameAgent
import board_setup
import time
import pygame
import importlib

class GameBoard(Scene):
    def __init__(self, game_manager, player_setup_list):
        super().__init__(game_manager, bg_color=(204,230,207))

        # Screen dimensions
        self.screen_width = game_manager.screen.get_width()
        self.screen_height = game_manager.screen.get_height()

        # Board spaces
        self.spaces = board_setup.load_test_board(self.screen_width, self.screen_height)
        head_space = self.spaces.get_head_space()
        curr_space = head_space
        first_iteration = True
        while True:
            if curr_space == head_space and not first_iteration:
                break
            first_iteration = False
            self.add_entity(curr_space) # add to the scene's entity list
            curr_space = curr_space.get_next_space()
            if curr_space is None:
                break

        # Roll dice button
        self.dice_button = Button(self.screen_width * 0.5, self.screen_height * 0.5, "Roll!", self.roll_dice)
        self.add_entity(self.dice_button)

        # Actual dice
        self.dice1 = Dice(self.screen_width * 0.4, self.screen_height * 0.6)
        self.dice2 = Dice(self.screen_width * 0.6, self.screen_height * 0.6)
        self.add_entity(self.dice1)
        self.add_entity(self.dice2)
        self.dice_res1 = None
        self.dice_res2 = None

        # Player setup
        self.players = []
        for p in player_setup_list:
            new_player = GameAgent(p["name"], self.spaces.get_head_space(), p["token"])
            self.players.append({
                "game_agent": new_player,
                "called_on_land": True,
                "path_size": 0
            })
            self.add_entity(new_player)
        self.player_turn = 0

        print(f"Loaded {len(self.players)} players.")

        super().on_load()

    def rolled_dice_callback(self):
        result = self.dice_res1 + self.dice_res2
        self.players[self.player_turn]["game_agent"].jump_spaces(result)
    
    def roll_dice(self):
        """BUTTON ACTION: roll both dice"""
        self.dice_res1 = self.dice1.roll()
        self.dice_res2 = self.dice2.roll(self.rolled_dice_callback)

    def on_pass(self, player, space):
        """SCENE EVENT: Called when a player ever jumps on a space, but not when they land on one."""
        self.set_camera_quad(space.quadrant_idx)

    def on_land(self, player, space):
        """SCENE EVENT: Called when a player lands on a space (final destination)."""

        # Space type events
        # goes through /scenes/events/ and calls the respective *_event.py module
        module_name = space.space_type.lower().replace(" ", "_") + "_event"
        full_module_path = f"scenes.events.{module_name}"
        try:
            mod = importlib.import_module(full_module_path)
            class_name = "".join(word.capitalize() for word in space.space_type.split()) + "Event"
            event_class = getattr(mod, class_name)
            event_class(self, player, space).on_land()
        except (ModuleNotFoundError, AttributeError):
            print(f"No event found for space type: {space.space_type}")

        self.set_camera_quad(0)
        self.player_turn = (self.player_turn + 1) % len(self.players)

    def handle_events(self, events):
        super().handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                # toggle player camera focus
                if event.key == pygame.K_SPACE:
                    if self.current_scale_offset_idx == 0:
                        self.set_camera_quad(self.players[self.player_turn]["game_agent"].current_space.quadrant_idx)
                    else:
                        self.set_camera_quad(0)

    def update(self):
        super().update()

        # Handles the space landing and passing event
        for p in self.players:
            if p["game_agent"].moving:
                p["called_on_land"] = False
            if not p["game_agent"].moving and not p["called_on_land"]:
                self.on_land(p["game_agent"], p["game_agent"].get_current_space())
                p["called_on_land"] = True
            if p["game_agent"].moving and len(p["game_agent"].move_path) != p["path_size"]:
                self.on_pass(p["game_agent"], p["game_agent"].current_space)
                p["path_size"] = len(p["game_agent"].move_path)