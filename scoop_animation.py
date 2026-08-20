import pygame
import consts



class scoop(pygame.sprite.Sprite):
    def __init__(scoop, pos_x, pos_y):
        super().__init__()
        scoop.scoop_sprites = []
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-1.png"), 0.1))
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-2.png"), 0.1))
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-3.png"), 0.1))
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-4.png"), 0.1))
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-5.png"), 0.1))
        scoop.scoop_sprites.append(pygame.transform.scale_by
                                     (pygame.image.load("scooping/scooping-6.png"), 0.1))
        scoop.current_sprite = 0
        scoop.image = scoop.scoop_sprites[scoop.current_sprite]

        scoop.rect = scoop.image.get_rect()
        scoop.rect.topleft = [pos_x, pos_y]


    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.scoop_sprites):
            self.current_sprite = 0
            consts.scooping=False


        self.image = self.scoop_sprites[int(self.current_sprite)]


scoop_sprites = pygame.sprite.Group()
scoop =scoop(consts.SPOON_INITIAL_X, consts.SPOON_INITIAL_Y)
scoop_sprites.add(scoop)




