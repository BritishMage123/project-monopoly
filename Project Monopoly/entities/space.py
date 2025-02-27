import pygame
from entities.entity import Entity

class Space(Entity):
    def __init__(self, x, y, size, space_type, pass_reward, text, image):
        super().__init__(x, y, size, size, centered=False)
        self.space_type = space_type
        self.pass_reward = pass_reward
        self.text = text
        self.image = image
        self.next_space = None

    def get_coordinates(self):
        """Returns (
            (x1, y1) -> top left,
            (x2, y2) -> bottom right,
            (mx, my) -> midpoint
        )"""
        return (self.rect.topleft, self.rect.bottomright, self.rect.center)

    def set_next_space(self, next_space):
        self.next_space = next_space

    def get_next_space(self):
        return self.next_space
    
    def render(self, screen):
        # Draw filled red rectangle
        pygame.draw.rect(
            screen,
            (251,57,45),  # Red color
            self.rect
        )

        # Draw black outline 1
        pygame.draw.rect(
            screen,
            (0, 0, 0),  # Black color
            self.rect,
            2  # Outline thickness
        )

        # Draw black outline 2
        pygame.draw.rect(
            screen,
            (0, 0, 0),  # Black color
            self.rect,
            2  # Outline thickness
        )

class LinkedSpaceList:
    def __init__(self):
        self.head_space = None

    def set_head_space(self, space):
        self.head_space = space

    def get_head_space(self):
        return self.head_space
