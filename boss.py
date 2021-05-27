import pygame
import random
from pygame.locals import *
from vector import Vector2
import math
clock = pygame.time.Clock()


class Boss(pygame.sprite.Sprite):
    def __init__(self,im, im2, im3):
        super().__init__()
        self.image = im
        self.rect = self.image.get_rect()
        self.baseImage = self.image
        self.mask = pygame.mask.from_surface(self.image, 200)
        self.speed_x = random.randrange(25, 75)
        self.life = 1000
        self.damage_image = im2
        self.damage_limit = im3
        self.size = self.image.get_size()

    def collide(self,damage):
        """lose hp when it hit bullet"""
        self.life -= damage

    def is_dead(self):
        if self.life <= 0:
            return True
        else:
            return False
    def get_hp(self):
        return int(self.life)

    def draw(self,x,y,win):
        self.rect = x,y
        pygame.draw.rect(win,(self.collide_part))

    def update(self):
        self.rect.x = 200
        if self.life <= 500 and self.life > 200:
            self.image = self.damage_image
        elif self.life <= 200 and self.life > 0:
            self.image = self.damage_limit
