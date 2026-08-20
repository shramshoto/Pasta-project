import pygame
import consts


screen=pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))

def draw_kitchen():
    pygame.init()
    KITCHEN_IMG=pygame.transform.scale(consts.KITCHEN_IMG, consts.KITCHEN_SIZE)
    screen.blit(KITCHEN_IMG, (0,0))

def draw_tomato():
    pygame.init()
    TOMATO_IMG=pygame.transform.scale(consts.TOMATO_IMG, consts.TOMATO_SIZE)
    screen.blit(TOMATO_IMG, consts.TOMATO_START_LOCATION)

def draw_message_a():
    pygame.draw.rect(screen, consts.BACKGROUND_COLOR, pygame.Rect(50, 50, 900, 400))
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    a_img = font.render(consts.MESSAGE_A, True, consts.COLOR)
    screen.blit(a_img, consts.FONT_LOCATION)

def draw_message_b():
    pygame.draw.rect(screen, consts.BACKGROUND_COLOR, pygame.Rect(50, 50, 900, 400))
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    b_img = font.render(consts.MESSAGE_B, True, consts.COLOR)
    screen.blit(b_img, consts.FONT_LOCATION)

def draw_message_c():
    pygame.draw.rect(screen, consts.BACKGROUND_COLOR, pygame.Rect(50, 50, 900, 400))
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    c_img = font.render(consts.MESSAGE_C, True, consts.COLOR)
    screen.blit(c_img, consts.FONT_LOCATION)
    collage_img = pygame.transform.scale(consts.collage_img, consts.TOMATO_SIZE)
    screen.blit(collage_img, (344, 330))

def draw_message_recipe():
    pygame.draw.rect(screen, consts.BACKGROUND_COLOR, pygame.Rect(900, 10, 100, 200))
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE_SMALL)
    re_img = font.render(consts.MESSAGE_RECIPE, True, consts.COLOR)
    screen.blit(re_img, consts.FONT_LOCATION_RECIPE)


def draw_empty_spoon():
    pygame.init()
    EMPTY_SPOON_IMG=pygame.transform.scale(consts.EMPTY_SPOON_IMG, consts.SPOON_SIZE)
    screen.blit(EMPTY_SPOON_IMG, (consts.SPOON_INITIAL_X,consts.SPOON_INITIAL_Y))

def drew_screen():
    draw_kitchen()
    draw_tomato()



