import pygame

pygame.init()

# Force a square resolution for the window
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 800

screen = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
x, y = screen.get_size()  # Will be (800, 800) in most cases
clock = pygame.time.Clock()
fps = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont("Arial", 32)

def clear_screen():
    screen.fill(BLACK)

def draw_starting_background():
    """Draws the initial menu background."""
    try:
        start_img = pygame.image.load("Graphics/Icons and backgrounds/Starting_Background.png").convert_alpha()
        start_img = pygame.transform.scale(start_img, (x, y))
        screen.blit(start_img, (0, 0))
    except FileNotFoundError:
        print("Warning: Background image not found, using black screen instead.")
        clear_screen()

def draw_text(text, text_col, x_coordinate, y_coordinate):
    """Draws text using the predefined font."""
    img = font.render(str(text), True, text_col)
    screen.blit(img, (x_coordinate, y_coordinate))

# Basic button class
class Button:
    def __init__(self, x_coordinate, y_coordinate, size_x, size_y, name):
        self.name = name
        self.image = pygame.image.load("Graphics/Icons and backgrounds/Icon_Button.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (size_x, size_y))
        self.rect = self.image.get_rect(center=(x_coordinate, y_coordinate))
        self.clicked = False

    def draw(self):
        screen.blit(self.image, self.rect.topleft)
        draw_text(self.name, WHITE, self.rect.x + 20, self.rect.y + 20)

    def is_hovered(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def clicked_on(self):
        if self.is_hovered():
            self.clicked = True

    def clicked_off(self):
        self.clicked = False
