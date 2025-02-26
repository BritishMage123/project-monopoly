import pygame
import interface_library
import game_instance

class MainMenu:
    def __init__(self):
        pygame.init()

        # Create buttons
        self.start_game_button = interface_library.Button(interface_library.x * 0.2, interface_library.y * 0.7, 400, 100, "Start Game")
        self.settings_button = interface_library.Button(interface_library.x * 0.5, interface_library.y * 0.7, 400, 100, "AI Settings")
        self.exit_button = interface_library.Button(interface_library.x * 0.8, interface_library.y * 0.7, 400, 100, "Exit")

        self.run = True

    def handle_events(self):
        """Handles user interactions such as clicking buttons."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button click
                    if self.start_game_button.is_hovered():
                        self.start_game_button.clicked_on()
                    if self.settings_button.is_hovered():
                        self.settings_button.clicked_on()
                    if self.exit_button.is_hovered():
                        self.exit_button.clicked_on()

    def update(self):
        """Handles button clicks."""
        if self.start_game_button.clicked:
            self.start_game_button.clicked_off()
            game = game_instance.GameInstance()
            game.run()  # Starts the game loop

        if self.settings_button.clicked:
            self.settings_button.clicked_off()
            print("AI Settings menu (not implemented yet).")

        if self.exit_button.clicked:
            self.exit_button.clicked_off()
            self.run = False

    def draw(self):
        """Draws the main menu background and buttons."""
        interface_library.draw_starting_background()
        self.start_game_button.draw()
        self.settings_button.draw()
        self.exit_button.draw()

    def run_menu(self):
        """Main menu loop."""
        while self.run:
            interface_library.clock.tick(interface_library.fps)
            self.handle_events()
            self.update()
            self.draw()  # FIX: Now draws the menu
            pygame.display.update()  # FIX: Ensures screen updates

        pygame.quit()

if __name__ == "__main__":
    menu = MainMenu()
    menu.run_menu()
