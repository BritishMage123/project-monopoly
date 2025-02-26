import pygame
import interface_library

class Entity:
    def __init__(self, name, is_bank=False):
        self.__balance = 0
        self.__name = name
        if is_bank:
            self.__balance = 100000  

class Player(Entity):
    def __init__(self, name, playerToken, linked_space_list, is_bank=False):
        super().__init__(name, is_bank)
        self.__current_space = linked_space_list.get_head_space()
        self.playerToken = pygame.transform.scale(playerToken, (interface_library.x * (2 / 15), interface_library.y * (1 / 15)))
        self.x_coordinate, self.y_coordinate = self.__current_space.get_coordinates()[2]

    def get_current_space(self):
        return self.__current_space

    def jump_spaces(self, num_spaces=0):
        """Moves player forward through LinkedSpaceList."""
        num_spaces=1
        for _ in range(num_spaces):
            self.__current_space = self.__current_space.get_next_space()

        self.x_coordinate, self.y_coordinate = self.get_current_space().get_coordinates()
        return self.__current_space

    def draw_player(self):
        """Draw player on screen at their current position."""
        interface_library.screen.blit(self.playerToken, (self.x_coordinate, self.y_coordinate))

class PlayablePlayer:
    def __init__(self, name, image, space_list):
        self.name = name
        self.image = image
        self.spaces = space_list
        self.current_space = space_list.get_head_space()

        # Start the player on the midpoint of the current_space
        (x1, y1), (x2, y2), (mx, my) = self.current_space.get_coordinates()
        self.x = mx
        self.y = my

    def jump_spaces(self, num_spaces):
        """
        Advances the player 'num_spaces' steps around the board,
        and updates the player's (x, y) to the midpoint of the new space.
        """
        num_spaces=1
        for _ in range(num_spaces):
            self.current_space = self.current_space.get_next_space()

        # Land on final space, move to that midpoint
        (x1, y1), (x2, y2), (mx, my) = self.current_space.get_coordinates()
        self.x = mx
        self.y = my

    def draw_player(self):
        """
        Draw the player's token so that it is centered on (self.x, self.y).
        """
        rect = self.image.get_rect(center=(self.x, self.y))
        interface_library.screen.blit(self.image, rect)

class NPCPlayer(Player):
    def __init__(self, name, playerToken, linked_space_list):
        super().__init__(name, playerToken, linked_space_list, is_bank=False)
        self.x_coordinate, self.y_coordinate = self.get_current_space().get_coordinates()[2]
