import pygame
import consts


class pour(pygame.sprite.Sprite):
    def __init__(pour, pos_x, pos_y):
        super().__init__()
        pour.pour_sprites = []
        pour.pour_sprites.append(pygame.transform.scale_by
                                   (pygame.image.load("scooping/scooping-1.png"), 0.1))
        pour.pour_sprites.append(pygame.transform.scale_by
                                   (pygame.image.load('pouring/pouring-2.png'), 0.1))
        pour.pour_sprites.append(pygame.transform.scale_by
                                  (pygame.image.load('pouring/pouring-3.png'), 0.1))
        pour.pour_sprites.append(pygame.transform.scale_by
                                   (pygame.image.load('pouring/pouring-4.png'), 0.1))
        pour.pour_sprites.append(pygame.transform.scale_by
                                   (pygame.image.load('pouring/pouring-5.png'), 0.1))
        pour.current_sprite = 0
        pour.image = pour.pour_sprites[pour.current_sprite]


    def update(self):
        self.current_sprite += 0.1

        if self.current_sprite >= len(self.pour_sprites):
            self.current_sprite = 0
            consts.SPOON["state"] = True

        self.image = self.pour_sprites[int(self.current_sprite)]

pour_sprites = pygame.sprite.Group()
pour = pour(100, 100)
pour_sprites.add(pour)