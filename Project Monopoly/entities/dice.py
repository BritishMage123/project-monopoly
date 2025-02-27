import pygame
import random
from entities.animated_entity import AnimatedEntity

class Dice(AnimatedEntity):
    def __init__(self, x, y):
        # List of dice face images (indexed 0-5)
        dice_faces = [
            "assets/dice_1.png",
            "assets/dice_2.png",
            "assets/dice_3.png",
            "assets/dice_4.png",
            "assets/dice_5.png",
            "assets/dice_6.png"
        ]

        super().__init__(x, y, 60, 60, dice_faces, frame_duration=0.1)

        self.final_value = random.randint(1, 6)  # The final dice roll (1-6)

    def roll(self):
        """Starts the rolling animation for 1 second and determines final dice value."""
        if not self.animating:  # Prevent double clicks
            self.final_value = random.randint(1, 6)  # Get a dice value (1-6)
            self.start_animation(loop=True, duration=1.0)  # Animate for 1 second
        return self.final_value

    def update(self):
        """After animation duration, display the final dice roll."""
        super().update()  # Handle frame updates

        if not self.animating:  # If animation stopped, set final face
            self.current_frame = self.final_value - 1
