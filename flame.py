import pygame as py
import math
import random
import pygame.sprite
from vector import Vector2


class Fire(pygame.sprite.Sprite):
    def __init__(self, image1, xy = None):
        super().__init__()
        self.x = 740
        self.y = 540
        self.image = image1
        self.baseimage = image1
        self.rect = self.image.get_rect()


        if xy == None:
            self.rect = self.rect


    def is_dead(self):
            self.kill()


    def update(self, time):

        self.rect.x = self.rect.x + self.x
        self.rect.y = self.rect.y + self.y
        if time > .033:
            self.is_dead()