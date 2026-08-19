import pygame
import consts
from consts import PAN_IMG

screen=pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))
screen.fill(consts.BACKGROUND_COLOR)
'''def draw_kitchen():
    pygame.init()
    KITCHEN_IMG=pygame.transform.scale(consts.KITCHEN_IMG, consts.KITCHEN_SIZE)
    screen.blit(KITCHEN_IMG, (0,0))'''

'''def draw_pasta():
    pygame.init()
    PASTA_IMG=pygame.transform.scale(consts.PASTA_IMG, consts.PASTA_SIZE)
    screen.blit(PASTA_IMG, (consts.PASTA_START_LOCATION) )
    pygame.display.update()'''

def draw_pot():
    pygame.init()
    POT_IMG=pygame.transform.scale(consts.POT_IMG, consts.POT_SIZE)
    screen.blit(POT_IMG, (consts.POT_START_LOCATION))

def draw_pan():
    pygame.init()
    PAN_IMG=pygame.transform.scale(consts.PAN_IMG, consts.PAN_SIZE)
    screen.blit(PAN_IMG, (consts.PAN_START_LOCATION))

def draw_stove():
    pygame.init()
    STOVE_IMG=pygame.transform.scale(consts.STOVE_IMG, consts.STOVE_SIZE)
    screen.blit(STOVE_IMG, (consts.STOVE_START_LOCATION))

    STOVE_IMG = pygame.transform.scale(consts.STOVE_IMG, consts.STOVE_SIZE1)
    screen.blit(STOVE_IMG, (consts.STOVE_START_LOCATION1))

def draw_sauce():
    pygame.init()
    SAUCE_IMG = pygame.transform.scale(consts.SAUCE_IMG, (20, 10))
    screen.blit(SAUCE_IMG, (20, 30))