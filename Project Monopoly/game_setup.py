from properties import Market, Property
from space import LinkedSpaceList, Space
import json

def generate_market_from_json(json_file):
    with open(json_file, 'r') as file:
        market_data = json.load(file)

    market = Market()
    for property_id, property_data in market_data.items():
        new_property = Property(property_id, property_data["value"], property_data["base_tax"])
        market.add_game_property(new_property)

    return market

def generate_space_list_from_json(json_file):
    with open(json_file, 'r') as file:
        space_data = json.load(file)

    # initialize head space
    head_space = Space(
        space_type=space_data[0].get("space_type"),
        pass_reward=space_data[0].get("pass_reward"),
        text=space_data[0].get("name"),
        image=space_data[0].get("image")
    )

    curr_space = head_space
    for s in space_data[1:]: # loop everything after head space
        new_space = Space(
            space_type=s.get("space_type"),
            pass_reward=s.get("pass_reward"),
            text=s.get("name"),
            image=s.get("image")
        )
        curr_space.set_next_space(new_space)
        curr_space = curr_space.get_next_space()

    # link the last space to the head to make it circular
    curr_space.set_next_space(head_space)

    space_list = LinkedSpaceList()
    space_list.set_head_space(head_space)

    return space_list