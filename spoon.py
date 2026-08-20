import consts
import pour_animation
import scoop_animation
import Screen1


def animate_scoop():
    SPOON["state"] = True
    scoop_animation.scoop_sprites.draw(Screen1.screen)
    scoop_animation.scoop_sprites.update()

def animate_pour():
    SPOON["state"] = True
    pour_animation.pour_sprites.draw(Screen1.screen)
    pour_animation.pour_sprites.update()

def spoon_move():
    Screen1.draw_full_spoon()

SPOON = {"width": consts.SPOON_WIDTH, "height":consts.SPOON_HEIGHT, "obj_x":consts.SPOON_START_LOCATION[0],
         "obj_y":consts.SPOON_START_LOCATION[1],
        "animations": [animate_scoop(),spoon_move(), animate_pour()],
        "state": True}
