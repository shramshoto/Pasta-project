import pygame
import Screen1
import spoon

clock = pygame.time.Clock()
running = True
num = 0
max_num = len(spoon.SPOON)

def mouse_clicking_obj(num, mx, my, list):
    if list[num]["obj_x"]<mx<list[num]["obj_x"]+list[num]["width"] \
        and list[num]["obj_y"]<my<list[num]["obj_y"]+list[num]["height"]:
        return True
    return False

def do_animation(list, num):
    for i in range(len(list[num]["animations"])):
        if list[num]["state"]:
            list[num]["animations"][i]

def write():
    if event.key == pygame.K_1:
        Screen1.draw_message_a()
    elif event.key == pygame.K_2:
        Screen1.draw_message_b()
    elif event.key == pygame.K_3:
        Screen1.draw_message_c()

while running:
    pygame.init()
    pygame.display.flip()

    while num < max_num:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mouse_clicking_obj(num, mx, my, spoon.SPOON):
                    do_animation(spoon.SPOON, num)
                    num += 1
                else:
                    pass
            elif event.type == pygame.KEYDOWN:
                write()

    else:
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

