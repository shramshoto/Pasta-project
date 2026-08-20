import pygame
import Screen1
import spoon
import consts

clock = pygame.time.Clock()
running = True
num = 0
max_num = len(spoon.SPOON)



def mouse_clicking_obj(mx, my):
    if spoon.SPOON["obj_x"]<mx<spoon.SPOON["obj_x"]+spoon.SPOON["width"] \
        and spoon.SPOON["obj_y"]<my<spoon.SPOON["obj_y"]+spoon.SPOON["height"]:
        return True
    return False

def do_animation():
    '''for i in range(len(spoon.SPOON["animations"])):
        #if consts.state:
        spoon.SPOON["animations"][i]'''
    spoon.animate_scoop()
    pygame.display.flip()
    spoon.spoon_move()
    pygame.display.flip()
    spoon.animate_pour()
    pygame.display.flip()

def write():
    if event.key == pygame.K_1:
        Screen1.draw_message_a()
        pygame.display.flip()
    elif event.key == pygame.K_2:
        Screen1.draw_message_b()
        pygame.display.flip()
    elif event.key == pygame.K_3:
        Screen1.draw_message_c()
        pygame.display.flip()

while running:

    pygame.init()
    Screen1.drew_screen()
    Screen1.draw_empty_spoon()
    pygame.display.flip()

    while num < max_num:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                consts.scooping = True

                if consts.scooping:
                    spoon.animate_pour()
                elif consts.pouring:
                    spoon.animate_scoop()
                elif consts.move:
                    spoon.spoon_move()

            elif event.type == pygame.KEYDOWN:
                write()

    else:
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()

