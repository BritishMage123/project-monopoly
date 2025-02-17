from properties import Property

class Space:
    def __init__(self, space_type=None, pass_reward=None, text=None, image=None, coordinates=None):
        self.__next_space = None
        self.__space_type = space_type
        self.__pass_reward = pass_reward
        self.__text = text
        self.__image = image
        self.__coordinates = coordinates

    def set_next_space(self, next_space):
        self.__next_space = next_space

    def get_next_space(self):
        return self.__next_space

    def set_space_type(self, space_type):
        self.__space_type = space_type
    
    def get_space_type(self):
        return self.__space_type
    
    def set_pass_reward(self, reward):
        self.__pass_reward = reward
    
    def get_pass_reward(self):
        return self.__pass_reward
    
    def set_text(self, text):
        self.__text = text

    def get_text(self):
        return self.__text
    
    def set_image(self, image):
        self.__image = image

    def get_image(self):
        return self.__image
    
    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_coordinates(self):
        return self.__coordinates

class LinkedSpaceList:
    """
    This is a linked list representation for board spaces.
    """
    def __init__(self):
        self.__head_space = None

    def set_head_space(self, head_space: Space):
        self.__head_space = head_space

    def get_head_space(self):
        return self.__head_space
    
    def get_space_from_property(self, property: Property):
        # TODO: walk through linked list until space text matches property name
        pass