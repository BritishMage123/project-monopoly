import pygame
from ui.ui_element import UIElement

class Button(UIElement):
    def __init__(self, x, y, text, action, width=200, height=50, centered=True):
        super().__init__(x, y, width, height, text, centered=centered)
        self.action = action
        self.default_color = (100, 100, 255)
        self.hover_color = (150, 150, 255)
        self.current_color = self.default_color

    def handle_events(self, events):
        """Detects clicks and triggers action."""
        mouse_pos = pygame.mouse.get_pos()
        mouse_over = self.rect.collidepoint(mouse_pos)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouse_over:
                self.action()  # Execute assigned function

        # Change color on hover
        self.current_color = self.hover_color if mouse_over else self.default_color

    def render(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect)
        self.render_text(screen)
