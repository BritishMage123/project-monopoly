import pygame
import Interface_library as Game_Library


def draw_background_board(x_location, y_location, x_scale, y_scale):
    board_slot_img = pygame.image.load(rf"Graphics\Map\game slot.png").convert_alpha()
    board_slot_img = pygame.transform.scale(board_slot_img, (x_scale, y_scale))
    Game_Library.screen.blit(board_slot_img, (x_location, y_location))


class Space:
    def __init__(self, space_type, x_coordinate, y_coordinate, rotation):
        self.space_type = space_type
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.space_rotation = rotation
        if self.space_type == "Property":
            self.board_slot_img = pygame.image.load(rf"Graphics\Map\game slot.png").convert_alpha()
        else:
            self.board_slot_img = pygame.image.load(rf"Graphics\Map\Corner_slot.png").convert_alpha()
        self.board_slot_img = pygame.transform.rotate(self.board_slot_img, self.space_rotation)
        self.rect = self.board_slot_img.get_rect()
        self.rect.center = (x_coordinate, y_coordinate)

    def scale(self):
        if self.space_type == "corner":
            x_scale = Game_Library.x * (2 / 13)
            y_scale = Game_Library.y * (2 / 13)
        elif self.space_rotation == 0 or self.space_rotation == 180:
            x_scale = Game_Library.x * (1 / 13)
            y_scale = Game_Library.y * (2 / 13)
        else:
            x_scale = Game_Library.x * (2 / 13)
            y_scale = Game_Library.y * (1 / 13)
        return x_scale, y_scale

    def draw(self):
        x_scale, y_scale = self.scale()
        Game_Library.screen.blit(self.board_slot_img, (self.x_coordinate, self.y_coordinate))
        self.board_slot_img = pygame.transform.scale(self.board_slot_img, (x_scale, y_scale))

    def get_x_and_y(self):
        return self.x_coordinate, self.y_coordinate
    #def set_x_and_y(self, x, y):


def load_test_board():
    spaces = []

    # makes the 1st space
    space = Space("corner", Game_Library.x * (11 / 13), Game_Library.y * (11 / 13), 0)
    spaces.append(space)

    # makes spaces 2-10
    for i in range(2, 11):
        space = Space("Property", Game_Library.x * (i / 13), Game_Library.y * (11 / 13), 0)
        spaces.append(space)

    # makes the 11th space
    space = Space("corner", Game_Library.x * (0 / 13), Game_Library.y * (11 / 13), 0)
    spaces.append(space)

    # makes the spaces 12-20
    for i in range(2, 11):
        space = Space("Property", Game_Library.x * (0 / 13), Game_Library.y * (i / 13), 270)
        spaces.append(space)

    # makes the 21st space
    space = Space("corner", Game_Library.x * (0 / 13), Game_Library.y * (0 / 13), 0)
    spaces.append(space)

    # makes the spaces 22-30
    for i in range(2, 11):
        space = Space("Property", Game_Library.x * (i / 13), Game_Library.y * (0 / 13), 180)
        spaces.append(space)

    # makes the 31st space
    space = Space("corner", Game_Library.x * (11 / 13), Game_Library.y * (0 / 13), 0)
    spaces.append(space)
    # makes the spaces 32-40
    for i in range(2, 11):
        space = Space("Property", Game_Library.x * (11 / 13), Game_Library.y * (i / 13), 90)
        spaces.append(space)

    return spaces
