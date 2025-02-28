import pygame
import json
from entities.entity import Entity
from properties import Property

class Space(Entity):
    def __init__(self, x, y, size, space_type, pass_reward, text, icon, color):
        super().__init__(x, y, size, size, centered=False)
        self.space_type = space_type
        self.pass_reward = pass_reward
        self.text = text
        self.icon = icon
        self.color = color
        self.property = None
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
        # Get space color
        with open("ui/colors.json", 'r') as file:
            colors = json.load(file)
        color_rgb = colors[self.color]

        # Draw top rectangle
        if self.space_type == "PROPERTY":
            top_rect = (self.rect.topleft[0], self.rect.topleft[1], self.rect.width, self.rect.height // 3)
        else:
            top_rect = self.rect
        pygame.draw.rect(
            screen,
            color_rgb,
            top_rect
        )

        # Draw border outline
        pygame.draw.rect(
            screen,
            (0, 0, 0),  # Black color
            self.rect,
            2  # Outline thickness
        )

        # Draw top border outline 2 if property
        if self.space_type == "PROPERTY":
            pygame.draw.rect(
                screen,
                (0, 0, 0),  # Black color
                top_rect,
                1  # Outline thickness
            )
            
        # Write the center of self.rect
        font = pygame.font.Font(None, 20)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

        # Write price if property
        if self.space_type == "PROPERTY":
            text_surface = font.render(f"£{self.property.get_value()}", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            scale_pos = 0.7     # set this to whatever scalar 0-1
            screen.blit(text_surface, (text_rect.topleft[0],
                                       text_rect.topleft[1] + (self.rect.height // 2) * scale_pos, # ensures not written outside space
                                       text_rect.width, text_rect.height))

class LinkedSpaceList:
    def __init__(self):
        self.head_space = None

    def set_head_space(self, space):
        self.head_space = space

    def get_head_space(self):
        return self.head_space
