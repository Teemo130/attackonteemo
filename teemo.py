import pygame as py
import math
import random
import pygame.sprite
from vector import Vector2

class Teemo(pygame.sprite.Sprite):
    def __init__(self, image1,image3, xy = None):
        super().__init__()
        self.x = 0
        self.y = 0
        self.z = 900
        self.o = 700
        self.image = image1
        self.baseimage = image1
        self.rect = self.image.get_rect()
        self.pos = (self.x,self.y)
        self.gif = []
        self.hp = 1000
        self.frame = 0
        self.image3 = image3
        self.timer = 0
        self.destination = pygame.mouse.get_pos()
        self.damge = 1


        if xy == None:
            self.rect = self.rect

    def collide(self,other_group,damge):
        if pygame.sprite.spritecollide(self,other_group, False):
            self.hp -= damge

    def lose_hp(self, damge):
        self.hp -= damge

    def health(self):
        return str(self.hp)

    def is_dead(self):
        if self.hp <= 0:
            return True

    def damage_dult(self, boost):
        self.damge += boost
        return self.damge

    def rotate(self):
        rel_x, rel_y = pygame.mouse.get_pos()
        rel_x -= self.z + self.x
        rel_y -= self.o + self.y
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        self.image = py.transform.rotate(self.image3[self.timer], angle)
        self.rect = self.image.get_rect()

    def set_pos(self):
        self.rect.x, self.rect.y = 900, 450
        return self.rect.x, self.rect.y

    def movement(self, x_1=int, y_1=int):
        self.x += x_1
        self.y += y_1
    def update(self, time_passed):

        while random.randrange(1,6) == 1:
            self.timer += 1
            if self.timer >= 4:
                self.timer -= 4

        self.set_pos()
        self.rotate()
        self.rect.x = self.rect.x + self.x + self.z
        self.rect.y = self.rect.y + self.y + self.o






