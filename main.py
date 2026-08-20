import pygame,sys
import Screen1
import consts

pygame.init()
clock = pygame.time.Clock()
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    Screen1.draw_kitchen()
    Screen1.draw_tomato()
    '''Screen1.draw_message_a()
    Screen1.draw_message_b()
    Screen1.draw_message_c()'''
    clock.tick(60)

# clock = pygame.time.Clock()
running = True
num = 0
def mouse_clicking_obj(num, mx, my, list):
    if list[num]["obj_x"]<mx<list[num]["obj_x"]+list[num]["width"] \
        and list[num]["obj_y"]<my<list[num]["obj_y"]+list[num]["height"]:
        num += 1
        return True
    return False

'''while running:
    pygame.init()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mouse_clicking_obj(num, mx, my, consts.appearance):
                #DO ANIMATION
                pass
            else:
                pass

pygame.quit()'''

'''def mouse_clicking_obj(num, mx, my, list):
    if list[num]["obj_x"]<mx<list[num]["obj_x"]+list[num]["width"] \
        and list[num]["obj_y"]<my<list[num]["obj_y"]+list[num]["height"]:
        num += 1
        return True
    return False'''
