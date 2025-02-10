import pygame
import Interface_library as Game_Library


# creates the 3 buttons for the menu
Start_Game = Game_Library.Button(Game_Library.x * (1 / 10), Game_Library.y * (7 / 10), Game_Library.button_image, 400,
                                 100)
Settings = Game_Library.Button(Game_Library.x * (4 / 10), Game_Library.y * (7 / 10), Game_Library.button_image, 400,
                               100)
Exit = Game_Library.Button(Game_Library.x * (7 / 10), Game_Library.y * (7 / 10), Game_Library.button_image, 400, 100)

run = True
while run:
    Game_Library.clock.tick(Game_Library.fps)
    Game_Library.draw_starting_background()
    #Game_Library.draw_starting_screen("Property Tycoon", 4.4, 1.5, 0.1, 0.1)
    Start_Game.draw("Start Game")
    Settings.draw("Ai Settings")
    Exit.draw("Exit")

    # checks if the player has started the game
    if Start_Game.Clicked:
        Start_Game.clicked_off()
        print("button 1 works")

    # user gets to set the screen size
    if Settings.Clicked:
        Settings.clicked_off()
        print("button 2 works")

    # exits the player when clicked
    if Exit.Clicked:
        Exit.clicked_off()
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button?
                Start_Game.clicked_on()
                Settings.clicked_on()
                Exit.clicked_on()

    pygame.display.update()

pygame.quit()
# sys.exit()
