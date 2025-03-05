import pygame
from ui.ui_element import UIElement

class TextBox(UIElement):
    def __init__(self, x, y, width, height, placeholder="Enter text...", font_size=32, centered=True, text_color="black"):
        super().__init__(x, y, width, height, "", font_size, centered=centered, text_color=text_color)
        self.placeholder = placeholder
        self.active = False
        self.max_length = 20

    def handle_events(self, events):
        """Handles input and focus detection."""
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.active = self.rect.collidepoint(event.pos)

            elif event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < self.max_length and event.unicode.isprintable():
                    self.text += event.unicode

    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        self.render_text(screen)
