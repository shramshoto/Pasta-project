import pygame
import consts

WINDOW=pygame.display.set_mode((consts.WINDOW_WIDTH,consts.WINDOW_HEIGHT))
WINDOW.fill((255,230,247))

def display():
    pygame.display.flip()