import pygame as py
import math
import random
import pygame.sprite
from vector import Vector2


class Fire(pygame.sprite.Sprite):
    def __init__(self, image1):
        super().__init__()
        self.x = 740
        self.y = 540
        self.image = image1
        self.baseimage = image1
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = self.x
        self.rect.y = self.y


    def is_dead(self):
            self.kill()


    def update(self, time):

        if time > .033:
            self.is_dead()