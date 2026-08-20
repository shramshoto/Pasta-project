import pygame
import Screen1
import spoon
import consts

clock = pygame.time.Clock()

num = 0
max_num = len(spoon.SPOON)



def mouse_clicking_obj(mx, my):
    if spoon.SPOON["obj_x"]<mx<spoon.SPOON["obj_x"]+spoon.SPOON["width"] \
        and spoon.SPOON["obj_y"]<my<spoon.SPOON["obj_y"]+spoon.SPOON["height"]:
        return True
    return False

def do_animation():
    if consts.scooping:
        spoon.animate_scoop()
    elif consts.pouring:
        spoon.animate_pour()
    elif consts.move:
        spoon.spoon_move()

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


running = True
while running:

    pygame.init()
    Screen1.drew_screen()
    Screen1.draw_empty_spoon()
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                consts.scooping = True

            if event.type == pygame.KEYDOWN:
                write()

        do_animation()
        pygame.display.update()
        clock.tick(60)

pygame.quit()



