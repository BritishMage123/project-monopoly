import pygame
import interface_library
import board_setup
import dice
from entities import PlayablePlayer

class GameInstance:
    def __init__(self):
        pygame.init()

        # Create two dice and a dice roll button
        self.dice_1 = dice.Dice(2.5, 5)
        self.dice_2 = dice.Dice(6.5, 5)
        self.dice_button = interface_library.Button(
            interface_library.x * 0.5,
            interface_library.y * 0.5,
            200, 50,
            "Roll dice"
        )

        # Load the board (linked list of spaces)
        self.spaces = board_setup.load_test_board()

        # Create a single player
        player_img = pygame.image.load("Graphics/Icons and backgrounds/cart.png").convert_alpha()
        player_img = pygame.transform.scale(player_img, (100,100))
        self.player = PlayablePlayer("Player1", player_img, self.spaces)

        self.text_one = ""
        self.text_two = ""
        self.rolled = False
        self.animation_cooldown = 0
        self.game_run = True

    def draw_spaces(self):
        """
        Draws each space by retrieving its top-left and bottom-right corners
        from the space's coordinates.
        """

        head_space = self.spaces.get_head_space()
        curr_space = head_space
        first_iteration = True

        while True:
            if curr_space == head_space and not first_iteration:
                break
            first_iteration = False

            # Unpack the triple
            (x1, y1), (x2, y2), (mx, my) = curr_space.get_coordinates()
            width = x2 - x1
            height = y2 - y1

            # Draw filled red rectangle
            pygame.draw.rect(
                interface_library.screen,
                (251,57,45),  # Red color
                (x1, y1, width, height // 4)
            )

            # Draw black outline 1
            pygame.draw.rect(
                interface_library.screen,
                (0, 0, 0),  # Black color
                (x1, y1, width, height // 4),
                2  # Outline thickness
            )

            # Draw black outline 2
            pygame.draw.rect(
                interface_library.screen,
                (0, 0, 0),  # Black color
                (x1, y1, width, height),
                2  # Outline thickness
            )

            curr_space = curr_space.get_next_space()
            if curr_space is None:
                break

    def run(self):
        while self.game_run:
            interface_library.clock.tick(interface_library.fps)
            self.handle_events()
            self.handle_dice_roll()
            self.draw()

    def handle_dice_roll(self):
        """Handles dice rolling animation and updates player movement."""
        if self.animation_cooldown > 0:
            self.dice_1.update()
            self.dice_2.update()
            self.animation_cooldown -= 1
        elif self.rolled:
            movement_amount = self.dice_1.return_dice_value() + self.dice_2.return_dice_value()
            self.text_one = f"You will move {movement_amount} spaces"
            self.player.jump_spaces(movement_amount)
            self.rolled = False

    def handle_events(self):
        """Handles user interactions such as quitting and rolling the dice."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if self.dice_button.is_hovered():
                        self.dice_button.clicked_on()
                        self.rolled = True
                        self.animation_cooldown = 30
                        self.dice_1.roll_dice()
                        self.dice_2.roll_dice()

    def draw(self):
        interface_library.clear_screen()

        # Background
        interface_library.screen.fill((204,230,207))

        # Draw the board spaces
        self.draw_spaces()

        # Draw dice
        self.dice_1.draw(interface_library.screen, interface_library.x, interface_library.y)
        self.dice_2.draw(interface_library.screen, interface_library.x, interface_library.y)

        # Draw dice button
        self.dice_button.draw()

        # Draw the player
        self.player.draw_player()

        pygame.display.update()
