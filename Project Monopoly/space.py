import pygame

class Space:
    def __init__(self, space_type, pass_reward, text, image):
        """
        Each Space can represent a location on the board.
        __coordinates will store a triple:
           ((x1, y1), (x2, y2), (mx, my))
        where:
          - (x1, y1) is the top-left corner,
          - (x2, y2) is the bottom-right corner,
          - (mx, my) is the midpoint of that rectangle.
        """
        self.space_type = space_type
        self.pass_reward = pass_reward
        self.text = text
        self.image = image

        self.__coordinates = None
        self.next_space = None

    def set_coordinates(self, coords):
        """
        coords should be a triple of:
          ((x1, y1), (x2, y2), (mx, my))
        """
        self.__coordinates = coords

    def get_coordinates(self):
        """
        Returns ((x1, y1), (x2, y2), (mx, my))
        """
        return self.__coordinates

    def set_next_space(self, next_space):
        self.next_space = next_space

    def get_next_space(self):
        return self.next_space


class LinkedSpaceList:
    def __init__(self):
        self.head_space = None

    def set_head_space(self, space):
        self.head_space = space

    def get_head_space(self):
        return self.head_space
