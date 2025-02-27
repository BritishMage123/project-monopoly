import json
import os
from entities.space import LinkedSpaceList, Space

def generate_spaces(json_file, screen_width, screen_height):
    with open(json_file, 'r') as file:
        space_data = json.load(file)

    num_spaces = len(space_data)
    num_each_side = (num_spaces // 4) + 1

    # Setup sizes
    board_margin = 50
    board_width = screen_width - 2 * board_margin
    s = board_width // num_each_side

    # Directions, assuming clockwise orientation
    directions = [
        (-1,0),
        (0,-1),
        (1,0),
        (0,1)
    ]

    # Space generation
    space_list = LinkedSpaceList()

    def create_space(x1, y1, info):
        new_space = Space(x1, y1, s, info["space_type"], info["pass_reward"], info["name"], info["image"])
        return new_space

    # Start with bottom right
    x1, y1 = screen_width - board_margin - s, screen_height - board_margin - s
    curr_space = create_space(x1, y1, space_data[0])
    space_list.set_head_space(curr_space)

    d_idx = 0
    for i in range(1, num_spaces):
        d = directions[d_idx % 4]
        dx = d[0] * s
        dy = d[1] * s
        x1, y1 = x1 + dx, y1 + dy
        new_space = create_space(x1, y1, space_data[i])
        curr_space.set_next_space(new_space)
        curr_space = new_space
        if i % (num_each_side - 1) == 0:
            d_idx += 1

    curr_space.set_next_space(space_list.get_head_space())
    
    return space_list

def load_test_board(screen_width, screen_height):
    json_path = os.path.join("space_data.json")
    if not os.path.exists(json_path):
        raise FileNotFoundError(f"Missing JSON file: {json_path}")
    return generate_spaces(json_path, screen_width, screen_height)
