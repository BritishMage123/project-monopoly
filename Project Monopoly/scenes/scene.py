import pygame

class Scene:
    def __init__(self, game_manager, bg_color=(0,0,0)):
        self.game_manager = game_manager
        self.entities = []
        self.bg_color = bg_color

    def add_entity(self, entity):
        """Adds an entity to the scene."""
        self.entities.append(entity)

    def handle_events(self, events):
        for entity in self.entities:
            entity.handle_events(events)

    def update(self):
        for entity in self.entities:
            entity.update()

    def render(self, screen):
        screen.fill(self.bg_color)  # Clear screen
        for entity in self.entities:
            entity.render(screen)
