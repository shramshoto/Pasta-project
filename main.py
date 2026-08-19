import pygame,sys
import Screen1

pygame.init()
clock = pygame.time.Clock()
while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    #screen.draw_pasta()
    Screen1.draw_pot()
    Screen1.draw_pan()
    Screen1.draw_stove()
    #Screen1.draw_frame()
    '''Screen1.draw_message_a()
    Screen1.draw_message_b()
    Screen1.draw_message_c()'''
    clock.tick(60)