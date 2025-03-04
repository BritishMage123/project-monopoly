from scenes.scene import Scene
from ui.button import Button
from entities.dice import Dice
from entities.game_agent import GameAgent
import board_setup

class GameBoard(Scene):
    def __init__(self, game_manager):
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

        # Player
        # TODO: hard-coded for now
        # this is where we set up Player and AI agents
        self.player1 = GameAgent("Player 1", self.spaces.get_head_space(), "assets/cart.png")
        self.add_entity(self.player1)
        self.players = [
            {
                "game_agent": self.player1,
                "called_space_action": True
            }
        ]
    
    def roll_dice(self):
        """BUTTON ACTION: roll both dice"""
        res1 = self.dice1.roll()
        res2 = self.dice2.roll()
        if res1 == res2:
            print("DOUBLES!") # handle doubles
        result = res1 + res2
        self.player1.jump_spaces(result)

    def on_land(self, player, space):
        """SCENE EVENT: Called when a player lands on a space (final destination)."""

        # Space type events
        match space.space_type:
            case "PROPERTY":
                from scenes.events.property_event import PropertyEvent
                PropertyEvent(self, player, space).on_land()
            case "CHANCE":
                from scenes.events.chance_event import ChanceEvent
                ChanceEvent(self, player, space).on_land()
            case "JAIL":
                from scenes.events.jail_event import JailEvent
                JailEvent(self, player, space).on_land()
            case "GO":
                from scenes.events.go_event import GoEvent
                GoEvent(self, player, space).on_land()
            case "VISITING":
                from scenes.events.visiting_event import VisitingEvent
                VisitingEvent(self, player, space).on_land()
            case "COMMUNITY CHEST":
                from scenes.events.community_chest_event import CommunityChestEvent
                CommunityChestEvent(self, player, space).on_land()
            case "TAXES":
                from scenes.events.taxes_event import TaxesEvent
                TaxesEvent(self, player, space).on_land()

    def update(self):
        super().update()

        # Handles the space landing event
        for p in self.players:
            if p["game_agent"].moving:
                p["called_space_action"] = False
            if not p["game_agent"].moving and not p["called_space_action"]:
                self.on_land(p["game_agent"], p["game_agent"].get_current_space())
                p["called_space_action"] = True