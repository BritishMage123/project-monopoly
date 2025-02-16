# Importing pygame module
import pygame
import Interface_library as Game_Library
import Board_Setup as Map

dice_1 = Game_Library.Dice(2.5, 5)
dice_2 = Game_Library.Dice(6.5, 5)
dice_button = Game_Library.Button(Game_Library.x * (5 / 10), Game_Library.y * (5 / 10),
                                  400, 100, "Roll dice")


def load_game():
    text_one = ""
    text_two = ""
    rolled = False
    spaces = Map.load_test_board()
    # Draws the surface object to the screen.
    game_run = True
    animation_cooldown = 0
    while game_run:
        if animation_cooldown == 0:
            Game_Library.draw_starting_board()
            for i in range(len(spaces)):
                spaces[i].draw()
        Game_Library.draw_panel(6, 4, 2, 3.5, text_one, text_two)
        dice_1.draw()
        dice_2.draw()
        dice_button.draw()

        # if the dice button is clicked
        if dice_button.Clicked:
            print("click is detected")
            dice_button.clicked_off()
            rolled = True
            animation_cooldown = 30

        # this happens once the button is clicked showing the dice animation
        if animation_cooldown > 0:
            dice_1.roll_dice()
            dice_2.roll_dice()
            animation_cooldown -= 1

        # once the animation is finished the total value will be calculated and displayed
        if rolled is True and animation_cooldown == 0:
            movement_amount = dice_1.return_dice_value() + dice_2.return_dice_value()
            text_one = "You will move ", movement_amount, "spaces"
            rolled = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left mouse button?
                    dice_button.clicked_on()
        pygame.display.update()


