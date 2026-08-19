import pygame,sys

import animation
import consts
import screen

pygame.init()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    animation.lid_open(consts.LID,(500,250))
    screen.display()
    clock.tick(60)