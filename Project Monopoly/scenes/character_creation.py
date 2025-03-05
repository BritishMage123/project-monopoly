import pygame
from scenes.scene import Scene
from scenes.game_board import GameBoard
from ui.button import Button
from ui.text_box import TextBox
from ui.text_label import TextLabel
from entities.dice import Dice

class CharacterCreation(Scene):
    def __init__(self, game_manager):
        super().__init__(game_manager, bg_color=(204,230,207)) # always need to do this

        # Screen dimensions
        screen_width = game_manager.screen.get_width()
        screen_height = game_manager.screen.get_height()

        # UI Elements
        self.title_label = TextLabel(screen_width * 0.5, screen_height * 0.25,
                                    "Character Creator")
        self.new_character_button = Button(screen_width * 0.5, screen_height * 0.5,
                                    "New Character", self.new_character)

        # Add entities to scene so they are handled automatically
        self.add_entity(self.title_label)
        self.add_entity(self.new_character_button)

    def new_character(self):
        print("New character...")