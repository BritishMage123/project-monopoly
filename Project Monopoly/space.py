from enum import Enum
import json

class Space:
    def __init__(self, space_type=None, pass_reward=None, text=None, image=None):
        self.next_space = None
        self.space_type = space_type # this will probably be replaced by another object
                                    # for example, a "property" or "chance" object, or a parent of those two
        self.pass_reward = pass_reward
        self.text = text
        self.image = image

class LinkedSpaceList:
    """
    This is a linked list implementation for board spaces.
    It generates a circular chain of spaces from the data in space_data.json.
    """
    def __init__(self, space_data):
        self.head_space = None
        self.generate_list_from_json(space_data)

    def generate_list_from_json(self, json_file):
        with open(json_file, 'r') as file:
            space_info = json.load(file)

        # initialize head space
        self.head_space = Space(
            space_type=space_info[0].get("space_type"),
            pass_reward=space_info[0].get("pass_reward"),
            text=space_info[0].get("custom_text"),
            image=space_info[0].get("image")
        )

        curr_space = self.head_space
        for s in space_info[1:]: # loop everything after head space
            new_space = Space(
                space_type=s.get("space_type"),
                pass_reward=s.get("pass_reward"),
                text=s.get("custom_text"),
                image=s.get("image")
            )
            curr_space.next_space = new_space
            curr_space = new_space

        # link the last space to the head to make it circular
        curr_space.next_space = self.head_space

if __name__ == "__main__":
    space_list = LinkedSpaceList("space_data.json")

    curr_space = space_list.head_space
    first_space = curr_space
    while True:
        print(curr_space.image)
        curr_space = curr_space.next_space
        if curr_space == first_space:
            break  # Stop after completing a full cycle