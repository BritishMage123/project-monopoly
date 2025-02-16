import pygame
import Interface_library as Game_Library
import Game_instance as Game
# creates the 3 buttons for the menu
Start_Game = Game_Library.Button(Game_Library.x * (2 / 10), Game_Library.y * (7 / 10),
                                 400, 100, "Start Game")
Settings = Game_Library.Button(Game_Library.x * (5 / 10), Game_Library.y * (7 / 10),
                               400, 100, "Ai Settings")
Exit = Game_Library.Button(Game_Library.x * (8 / 10), Game_Library.y * (7 / 10), 400,
                           100, "Exit")
run = True
while run:
    Game_Library.clock.tick(Game_Library.fps)
    Game_Library.draw_starting_background()
    Start_Game.draw()
    Settings.draw()
    Exit.draw()

    # checks if the player has started the game
    if Start_Game.Clicked:
        Start_Game.clicked_off()
        Game.load_game()

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
