import pygame

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
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
x, y = screen.get_size()
clock = pygame.time.Clock()
fps = 60


# draws background
def draw_starting_background():
    # start screen image
    start_img = pygame.image.load(f"Graphics\Icons and backgrounds\Start_background.png").convert_alpha()
    start_img = pygame.transform.scale(start_img, (x, y))
    screen.blit(start_img, (0, 0))


# for the map drawing
#map_img = pygame.image.load(f"Graphics\Map\Soviet Union Map.png").convert_alpha()
#map_img = pygame.transform.scale(map_img, (x, y))


# draws map
#def draw_map_background():
#    screen.blit(map_img, (0, 0))


# button image
button_image = pygame.image.load("Graphics\Icons and backgrounds/Icon_Button.png").convert_alpha()


# button class
class Button:
    def __init__(self, x_coordinate, y_coordinate, image, size_x, size_y):
        self.image = pygame.transform.scale(image, (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coordinate, y_coordinate)
        self.Clicked = False

    def draw(self, text):
        self.Name = text

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


# pannel for the ending menus
panel_menu_img = pygame.image.load(f"Graphics\Icons and backgrounds/Starting_Backround.png").convert_alpha()


def draw_starting_screen(text, x_text, y_text, x_cord, y_cord):
    screen.blit(panel_menu_img, (x * (x_cord / 10), y * (y_cord / 10)))
    draw_text(text, font, white, x * (x_text / 10), y * (y_text / 10))


# fuction for drawing pannel
def draw_panel(x_scale, y_scale, x_cord, y_cord, text_one, text_two):
    # draw panel rectangle
    panel_img = pygame.image.load(f"Graphics/Icons and backgrounds/Icon_Button.png").convert_alpha()
    panel_img = pygame.transform.scale(panel_img, (x * (x_scale / 10), (y * (y_scale / 10))))
    screen.blit(panel_img, (x * (x_cord / 10), (y * (y_cord / 10))))
    draw_text(text_one, font, white, x * (x_cord / 10) + 50, y * (y_cord / 10) + 50)
    draw_text(text_two, font, white, x * (x_cord / 10) + 50, y * (y_cord / 10) + 100)


class Dice:
    def __init__(self, x_coordinate, y_coordinate):
        self.dice_Faces = []
        self.x = x_coordinate
        self.y = y_coordinate
        for i in range(1, 7):
            dice_faces = pygame.image.load(f"Graphics\Icons and backgrounds/dice_{i}.png")
            self.dice_Faces.append(dice_faces)

    def draw(self, side):
        screen.blit(self.dice_Faces[side], (x * (self.x / 10), y * (self.y / 10)))
