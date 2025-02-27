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
        self.player1 = GameAgent("Player 1", self.spaces.get_head_space(), "assets/cart.png")
        self.add_entity(self.player1)
    
    def roll_dice(self):
        """BUTTON ACTION: roll both dice"""
        res1 = self.dice1.roll()
        res2 = self.dice2.roll()
        if res1 == res2:
            print("DOUBLES!") # handle doubles
        result = res1 + res2
        print(result)
        self.player1.jump_spaces(result)