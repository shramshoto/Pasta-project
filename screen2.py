import pygame
import consts

def draw_message_a(screen):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    a_img = font.render(consts.MESSAGE_A, True, consts.COLOR)
    screen.blit(a_img, consts.FONT_LOCATION)

def draw_message_b(screen):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    b_img = font.render(consts.MESSAGE_B, True, consts.COLOR)
    screen.blit(b_img, consts.FONT_LOCATION)

def draw_message_c(screen):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    c_img = font.render(consts.MESSAGE_C, True, consts.COLOR)
    screen.blit(c_img, consts.FONT_LOCATION)