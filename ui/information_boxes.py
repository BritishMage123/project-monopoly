import pygame
from ui.ui_element import UIElement


class InfoBox(UIElement):
    def __init__(self, x, y, width, height, title, firstLine, secondLine, font_size=32, centered=True):
        super().__init__(x, y, width, height, "", font_size, centered=centered)
        self.Title = title
        self.FirstLine = firstLine
        self.SecondLine = secondLine
        self.font = pygame.font.Font(None, font_size)


    def render_text(self, screen):
        title_surface = self.font.render(self.Title, True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.rect.centerx, self.rect.centery - 20))  # Move title up

        # Render the first line of text
        text_surface1 = self.font.render(self.FirstLine, True, (255, 255, 255))
        text_rect1 = text_surface1.get_rect(
            center=(self.rect.centerx, self.rect.centery + 5))  # Slightly below the center

        # Render the second line of text
        text_surface2 = self.font.render(self.SecondLine, True, (255, 255, 255))
        text_rect2 = text_surface2.get_rect(
            center=(self.rect.centerx, self.rect.centery + 30))  # Further below the first line

        # Blit (draw) the text onto the screen
        screen.blit(title_surface, title_rect)
        screen.blit(text_surface1, text_rect1)
        screen.blit(text_surface2, text_rect2)


    def render(self, screen):
        pygame.draw.rect(screen, (160, 82, 45), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        self.render_text(screen)

    def change_bal(self, new_balance):
        self.SecondLine ="Cash: " +str(new_balance)