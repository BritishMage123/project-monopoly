import pygame
import random

pygame.init()
# define colours
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
Black = (55, 55, 55)

# define fonts
font = pygame.font.SysFont("Amass MT Pro Black", 32)
# the screen settings
screen = pygame.display.set_mode((1920, 1080))
x, y = screen.get_size()
clock = pygame.time.Clock()
fps = 60


# draws background
def draw_starting_background():
    # start screen image
    start_img = pygame.image.load(rf"Graphics\Icons and backgrounds\Starting_Background.png").convert_alpha()
    start_img = pygame.transform.scale(start_img, (x, y))
    screen.blit(start_img, (0, 0))


def draw_starting_board():
    # start screen image
    board_img = pygame.image.load(rf"Graphics\Map\monopoly_board.png").convert_alpha()
    board_img = pygame.transform.scale(board_img, (x, y))
    screen.blit(board_img, (0, 0))


# button class
class Button:
    def __init__(self, x_coordinate, y_coordinate, size_x, size_y, name):
        self.Name = name
        self.image = pygame.transform.scale(pygame.image.load(
            rf"Graphics\Icons and backgrounds/Icon_Button.png").convert_alpha(), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.center = (x_coordinate, y_coordinate)
        self.Clicked = False

    def draw(self):
        # draw button
        screen.blit(self.image, (self.rect.x, self.rect.y))
        draw_text(self.Name, font, white, (self.rect.x + 20), (self.rect.y + 20))

    def clicked_on(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.Clicked = not self.Clicked

    def clicked_off(self):
        self.Clicked = not self.Clicked


# only for drawing text
def draw_text(text, text_font, text_col, x_coordinate, y_coordinate):
    img = text_font.render(str(text), True, text_col)
    width, height = img.get_size()
    img = pygame.transform.scale(img, (width * 1.7, height * 1.7))

    screen.blit(img, (x_coordinate, y_coordinate))


# draws up the background for the start scree
def draw_starting_screen(text, x_text, y_text, x_cord, y_cord):
    panel_menu_img = pygame.image.load(fr"Graphics\Icons and backgrounds/Starting_Background.png").convert_alpha()
    screen.blit(panel_menu_img, (x * (x_cord / 10), y * (y_cord / 10)))
    draw_text(text, font, white, x * (x_text / 10), y * (y_text / 10))


# function for drawing panel
def draw_panel(x_scale, y_scale, x_cord, y_cord, text_one, text_two):
    # draw panel rectangle
    panel_img = pygame.image.load(fr"Graphics\Icons and backgrounds/dice_background.png").convert_alpha()
    panel_img = pygame.transform.scale(panel_img, (x * (x_scale / 10), (y * (y_scale / 10))))
    screen.blit(panel_img, (x * (x_cord / 10), (y * (y_cord / 10))))
    draw_text(text_one, font, white, x * (x_cord / 10) + 50, y * (y_cord / 10) + 50)
    draw_text(text_two, font, white, x * (x_cord / 10) + 50, y * (y_cord / 10) + 100)


# class for the dice
class Dice:
    def __init__(self, x_coordinate, y_coordinate):
        self.dice_Faces = []
        self.x = x_coordinate
        self.y = y_coordinate
        self.dice_value = 1
        self.update_time = pygame.time.get_ticks()

        for i in range(1, 7):
            dice_faces = pygame.image.load(fr"Graphics\Icons and backgrounds/dice_{i}.png")
            self.dice_Faces.append(dice_faces)

    # draws the dice on the screen
    def draw(self):
        screen.blit(self.dice_Faces[self.dice_value], (x * (self.x / 10), y * (self.y / 10)))

    # upgrades dice image to give the visual affect of the dice rolling
    def roll_dice(self):
        animation_cooldown = 50
        self.update_time = pygame.time.get_ticks()
        # check if enough time has passed since the last update
        while pygame.time.get_ticks() - self.update_time < animation_cooldown:
            self.dice_value = random.randint(0, 5)

    def return_dice_value(self):
        return self.dice_value + 1
