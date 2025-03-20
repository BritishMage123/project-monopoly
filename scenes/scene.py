import pygame

class Scene:
    def __init__(self, game_manager, bg_color=(0, 0, 0)):
        self.game_manager = game_manager
        self.entities = []
        self.bg_color = bg_color
        # these set where the camera is placed this is done to see exactly where the pieces are moving
        self.camera_offsets_scalar = game_manager.screen.get_width() // 2
        self.camera_scales_offsets = [
            [0, 0, 1],        # normal
            [-1 * self.camera_offsets_scalar, -1 * self.camera_offsets_scalar, 2],  # bottom right
            [0, -1 * self.camera_offsets_scalar, 2],   # bottom left
            [0, 0, 2],    # top left
            [-1 * self.camera_offsets_scalar, 0, 2],   # top right
        ]
        self.current_scale_offset_idx = 0

    def on_load(self):
        # Called after the scene is finished loading with all its entities.
        self.set_camera_quad(0)

    def add_entity(self, entity):
        # Adds an entity to the scene.
        self.entities.append(entity)

    def remove_entity(self, entity):
        # removes an entity if it exists
        try:
            self.entities.remove(entity)
        except:
            pass

    def handle_events(self, events):
        # plays out the events that are scheduled in that scene (such as updating location of players)
        for entity in self.entities:
            entity.handle_events(events)

    def update(self):
        # updates the visual changes on the scene(such as actually showing the pieces moving )
        for entity in self.entities:
            entity.update()

    def render(self, screen):
        # draws the actual visual changes
        screen.fill(self.bg_color)
        for entity in self.entities:
            entity.render(screen)

    def set_camera_quad(self, quad_idx):
        # sets the camera to different locations
        self.current_scale_offset_idx = quad_idx
        offset_x, offset_y, scale = self.camera_scales_offsets[quad_idx]
        for entity in self.entities:
            entity.set_camera(offset_x, offset_y, scale)
