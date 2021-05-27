import pygame
import random
from pygame.locals import *
from vector import Vector2
import math
clock = pygame.time.Clock()


class Canon(pygame.sprite.Sprite):
    def __init__(self,im,  target, level, xy = None):
        super().__init__()
        self.image = im
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.baseImage = self.image
        self.mask = pygame.mask.from_surface(self.image, 200)
        self.speed_x = random.randrange(25, 75)
        self.life = 20
        self.level = level
        self.target = target
        self.destination = Vector2(self.target.rect.center)
        self.rect.center = Vector2(self.rect.center)




        if xy == None:
            x = random.randrange(2,5)
            if x == 2:
                self.rect.center = 0, random.randint(500,1000)
            if x == 3:
                self.rect.center = 1800,  random.randint(500,1000)
            if x == 4:
                self.rect.center = random.randint(0,1800), 1000

    def collide(self,damage):
        """lose hp when it hit bullet"""
        self.life -= damage

    def is_dead(self):
        if self.life <= 0:
            return True
        else:
            return False

    def rotate(self):
        rel_x, rel_y = self.destination
        rel_x -= self.rect.center[0]
        rel_y -= self.rect.center[1]
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        self.image = pygame.transform.rotate(self.baseImage, angle)
        x,y = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = x,y

    def update(self, time_passed):
        self.destination = self.target.rect.center
        self.destination = Vector2(self.target.rect.center)
        if self.rect.center != self.destination:
            vec_to_destination = self.destination - self.rect.center
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, time_passed * self.speed_x * self.level*.1)
            self.rect.center += travel_distance * heading
            self.rotate()