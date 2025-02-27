import pygame

class Entity:
    def __init__(self, x, y, width, height, centered=True):
        self.x = x - width // 2 if centered else x
        self.y = y - height // 2 if centered else y
        self.rect = pygame.Rect(self.x, self.y, width, height)

    def set_pos(self, x, y, centered=True):
        self.x = x - self.rect.width // 2 if centered else x
        self.y = y - self.rect.height // 2 if centered else y
        self.rect = pygame.Rect(self.x, self.y, self.rect.width, self.rect.height)

    def handle_events(self, events):
        """Override this method to handle events (e.g., clicks, keyboard input)."""
        pass

    def update(self):
        """Override this method for updates (e.g., movement, animations)."""
        pass

    def render(self, screen):
        """Override this method to draw the entity."""
        pass
