import pygame,sys
import Screen1
import consts

clock = pygame.time.Clock()
running = True
num = 0
max_num = len(consts.appearance)

def mouse_clicking_obj(num, mx, my, list):
    if list[num]["obj_x"]<mx<list[num]["obj_x"]+list[num]["width"] \
        and list[num]["obj_y"]<my<list[num]["obj_y"]+list[num]["height"]:
        return True
    return False

def do_animation(list, num):
    for i in range(len(list[num]["animations"])):
        if list[num]["state"]:
            list[num]["animations"][i]

while running:
    pygame.init()
    pygame.display.flip()

    while num < max_num:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if mouse_clicking_obj(num, mx, my, consts.appearance):
                    #do_animation(consts.appearance)
                    num += 1
                else:
                    pass
    else:
        running = False

    pygame.display.update()
    '''Screen1.draw_message_a()
        Screen1.draw_message_b()
        Screen1.draw_message_c()'''
    clock.tick(60)

pygame.quit()