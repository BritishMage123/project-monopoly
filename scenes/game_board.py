from scenes.scene import Scene
from ui.button import Button
from ui.text_label import TextLabel
from ui.text_box import TextBox
from entities.dice import Dice
from entities.game_agent import GameAgent
from ui.information_boxes import InfoBox
import board_setup
import pygame
import importlib
import glob
import os



class GameBoard(Scene):
    def __init__(self, game_manager, player_setup_list):
        super().__init__(game_manager, bg_color=(204, 230, 207))

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
            self.add_entity(curr_space)  # add to the scene's entity list
            curr_space = curr_space.get_next_space()
            if curr_space is None:
                break

        # Roll dice button
        self.dice_button = Button(self.screen_width * 0.3, self.screen_height * 0.5, "Roll!", self.roll_dice)

        # Actual dice
        self.dice1 = Dice(self.screen_width * 0.2, self.screen_height * 0.6)
        self.dice2 = Dice(self.screen_width * 0.4, self.screen_height * 0.6)
        self.dice_res1 = None
        self.dice_res2 = None

        # Turn indicator
        self.turn_indicator = TextLabel(self.screen_width * 0.3, self.screen_height * 0.7, "")

        # DEBUG: manual player move count
        self.debug_move_count = TextBox(self.screen_width * 0.5, self.screen_height * 0.55, width=50)

        # Player turn UI
        # Include dice and options to roll dice
        self.player_turn_ui = []
        self.player_turn_ui.append(self.dice1)
        self.player_turn_ui.append(self.dice2)
        self.player_turn_ui.append(self.dice_button)
        self.player_turn_ui.append(self.turn_indicator)
        if self.game_manager.debug_mode:
            self.player_turn_ui.append(self.debug_move_count)

        # Player setup
        self.players = []
        self.player_count = 0
        for p in player_setup_list:
            new_player = GameAgent(p["name"], self.spaces.get_head_space(), p["token"])
            self.players.append({
                "game_agent": new_player,
                "called_on_land": True,
                "path_size": 0
            })
            self.add_entity(new_player)
            self.player_count = self.player_count + 1
        self.player_turn = 0

        # player display
        self.TextBoxes = []
        print(self.player_count)
        for p in range(self.player_count):
            # textboxes of the different players
            if p == 0:
                Xcord = 0.65
                YCord = 0.2
            elif p == 1:
                Xcord = 0.875
                YCord = 0.2
            elif p == 2:
                Xcord = 0.65
                YCord = 0.5
            elif p == 3:
                Xcord = 0.875
                YCord = 0.5
            self.Textbox = InfoBox(self.screen_width * Xcord, self.screen_height * YCord,
                                    self.screen_width * 0.2, self.screen_height * 0.2,
                                    "Player" + str(p + 1), "Name: " + self.players[p]["game_agent"].get_name(),
                                    "Cash: " + str(self.players[p]["game_agent"].get_balance()))
            self.TextBoxes.append(self.Textbox)
            self.add_entity(self.Textbox)

        # Load events
        self.space_event_classes = {}
        event_path = "scenes/events"
        event_files = glob.glob(f"{event_path}/*_event.py")
        for filepath in event_files:
            filename = os.path.basename(filepath)
            space_type = filename.replace("_event.py", "").upper().replace("_", " ")
            module_name = filename[:-3]
            full_module_path = f"{event_path.replace('/', '.')}.{module_name}"
            class_name = "".join(word.capitalize() for word in space_type.split()) + "Event"
            try:
                mod = importlib.import_module(full_module_path)
                event_class = getattr(mod, class_name)
                self.space_event_classes[space_type] = event_class
            except (ModuleNotFoundError, AttributeError):
                print(f"No event found for space type: {space_type}")
                self.space_event_classes[space_type] = None

        self.show_player_turn_ui()
        print(f"Loaded {len(self.players)} players.")

        super().on_load()

    def rolled_dice_callback(self):
        # function to add the results of the 2 dice rolled
        result = self.dice_res1 + self.dice_res2
        if self.debug_move_count in self.player_turn_ui and self.debug_move_count.text != "":
            result = int(self.debug_move_count.text)
        self.players[self.player_turn]["game_agent"].jump_spaces(result)
        self.hide_player_turn_ui()

    def roll_dice(self):
        # BUTTON ACTION: roll both dice
        self.dice_res1 = self.dice1.roll()
        self.dice_res2 = self.dice2.roll(self.rolled_dice_callback, sound=True)

    def call_space_event(self, player, space, event_func):
        # calls the event associated with the space of the player
        event_class = self.space_event_classes.get(space.space_type)
        if event_class:
            event_instance = event_class(self, player, space)
            getattr(event_instance, event_func)()
        else:
            print(f"No event class cached for space type: {space.space_type}")

    def on_pass(self, player, space):
        # SCENE EVENT: Called when a player ever jumps on a space, but not when they land on one.
        self.call_space_event(player, space, "on_pass")
        self.set_camera_quad(space.quadrant_idx)

    def on_land(self, player, space):
        # SCENE EVENT: Called when a player lands on a space (final destination).

        self.set_camera_quad(0)
        self.hide_player_turn_ui()

        self.call_space_event(player, space, "on_land")

    def next_turn(self):
        # function to go to the next players turn
        self.player_turn = (self.player_turn + 1) % len(self.players)
        self.show_player_turn_ui()

    def hide_player_turn_ui(self):
        # hides player UI
        for e in self.player_turn_ui:
            self.remove_entity(e)

    def show_player_turn_ui(self):
        # displays all player UIs
        self.turn_indicator.text = f"{self.players[self.player_turn]['game_agent'].name}'s turn"
        for e in self.player_turn_ui:
            self.add_entity(e)

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
        # updates the animated actions on the board
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

        # updates the balance displayed on the text box of each player in case of changes
        for p in range(self.player_count):
            new_balance = self.players[p]["game_agent"].get_balance()
            self.TextBoxes[p].change_bal(new_balance)

    def render(self, screen):
        # draws the things that need to be displayed on the screen
        super().render(screen)