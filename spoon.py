import consts
import pour_animation
import scoop_animation
import Screen1
import pygame



def animate_scoop():
    Screen1.drew_screen()
    scoop_animation.scoop_sprites.draw(Screen1.screen)
    pygame.display.flip()
    scoop_animation.scoop_sprites.update()
    consts.move=True


def animate_pour():
    Screen1.drew_screen()
    pour_animation.pour_sprites.draw(Screen1.screen)
    pygame.display.flip()
    pour_animation.pour_sprites.update()



def spoon_move():
    pygame.init()
    Screen1.drew_screen()
    FULL_SPOON_IMG=pygame.transform.scale(consts.FULL_SPOON_IMG, consts.SPOON_SIZE)
    consts.SPOON_LOCATION=(consts.SPOON_SECOND_X,consts.SPOON_SECOND_Y)
    Screen1.screen.blit(FULL_SPOON_IMG, consts.SPOON_LOCATION)
    consts.move=False
    consts.pouring=True




SPOON = {"width": consts.SPOON_WIDTH, "height":consts.SPOON_HEIGHT, "obj_x":consts.SPOON_LOCATION[0],
         "obj_y":consts.SPOON_LOCATION[1]}
'''"animations": [animate_scoop(),spoon_move(), animate_pour()]'''
