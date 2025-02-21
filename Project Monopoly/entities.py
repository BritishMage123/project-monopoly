from space import LinkedSpaceList
import pygame
import Interface_library as Game_Library
import Board_Setup as Map

class Entity:
    def __init__(self, name, is_bank=False):
        self.__balance = 0
        self.__name = name
        if is_bank:
            self.balance = 100000

class Player(Entity):
    def __init__(self, name, playerToken,x_coordinate, y_coordinate , linked_space_list: LinkedSpaceList , is_bank=False):
        super().__init__(name, is_bank)
        self.__current_space = linked_space_list.get_head_space()
        self.playerToken = playerToken
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.playerToken = pygame.transform.scale(self.playerToken,
                                                  (Game_Library.x * (2 / 15), Game_Library.y * (1 / 15)))

    def get_current_space(self):
        return self.__current_space

    def jump_spaces(self, num_spaces=0):
        for i in range(num_spaces):
            if self.__current_space != 39:
                self.__current_space = self.__current_space.get_next_space()
            else:
                self.__current_space = 0
            self.x_coordinate, self.y_coordinate = Map.spaces[i].get_x_and_y()

        return self.__current_space
    def draw_player(self):
        Game_Library.screen.blit(self.playerToken, (self.x_coordinate, self.y_coordinate))




class PlayablePlayer(Player):
    def __init__(self):
        super().init()

class NPCPlayer(Player):
    def __init__(self):
        super().init()