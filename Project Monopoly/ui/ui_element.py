from entities.entity import Entity
import pygame 

class UIElement(Entity):
    def __init__(self, x, y, width, height, text="", font_size=32, centered=True):
        super().__init__(x, y, width, height, centered=centered)
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def render_text(self, screen):
        """Helper function to render text in the center of the element."""
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
