from space import LinkedSpaceList

class Entity:
    def __init__(self, name, is_bank=False):
        self.__balance = 0
        self.__name = name
        if is_bank:
            self.balance = 100000

class Player(Entity):
    def __init__(self, name, linked_space_list: LinkedSpaceList, is_bank=False):
        super().__init__(name, is_bank)
        self.__current_space = linked_space_list.get_head_space()

    def get_current_space(self):
        return self.__current_space
    
    def jump_spaces(self, num_spaces=1):
        for _ in range(num_spaces):
            self.__current_space = self.__current_space.get_next_space()
        return self.__current_space

class PlayablePlayer(Player):
    def __init__(self):
        super().init()

class NPCPlayer(Player):
    def __init__(self):
        super().init()