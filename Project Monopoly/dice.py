import pygame
import random

class Dice:
    def __init__(self, x_coordinate, y_coordinate):
        self.dice_faces = []
        self.x = x_coordinate
        self.y = y_coordinate
        self.dice_value = 1
        self.rolling = False
        self.animation_duration = 500  # Rolling animation lasts 500ms
        self.last_roll_time = pygame.time.get_ticks()

        # Load dice face images
        for i in range(1, 7):
            dice_face = pygame.image.load(f"Graphics/Icons and backgrounds/dice_{i}.png").convert_alpha()
            dice_face = pygame.transform.scale(dice_face, (100,100))
            self.dice_faces.append(dice_face)

    def draw(self, screen, x, y):
        """Draws the dice on the screen."""
        screen.blit(self.dice_faces[self.dice_value - 1], (x * (self.x / 10), y * (self.y / 10)))

    def start_roll(self):
        """Starts the rolling animation."""
        self.rolling = True
        self.last_roll_time = pygame.time.get_ticks()

    def update(self):
        """Handles dice rolling animation."""
        if self.rolling:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_roll_time < self.animation_duration:
                self.dice_value = random.randint(1, 6)  # Randomize dice value
            else:
                self.rolling = False  # Stop rolling after animation time

    def roll_dice(self):
        """Starts rolling and returns the final value when finished."""
        self.start_roll()

    def return_dice_value(self):
        """Returns the dice value after rolling has stopped."""
        return self.dice_value
