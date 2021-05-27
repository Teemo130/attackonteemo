import random

import pygame as py
import pygame.sprite
from vector import Vector2
import math

class Shroom(py.sprite.Sprite):
    def __init__(self,image,image2, location):
        super().__init__()
        self.speed = 10
        self.image = image
        self.image2 = image2
        self.x = location.rect.x
        self.y = location.rect.y
        self.mask = self.image.get_masks()
        self.rect = self.image.get_rect(center=location.rect.center)
        self.rotate()
        mouse = pygame.mouse.get_pos()
        self.destination = mouse
        self.destination = Vector2(mouse)
        self.second_count = 1
        if self.rect.center != self.destination:
            vec_to_destination = self.destination - self.rect.center
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, self.speed)
            self.rect.center += travel_distance * heading


    def rotate(self):
        rel_x, rel_y = py.mouse.get_pos()
        rel_x -= self.x
        rel_y -= self.y
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        self.image = py.transform.rotozoom(self.image, angle, 1)

    def collide(self,othergroup):
        if pygame.sprite.spritecollide(self, othergroup, False):
            self.image = self.image2
            self.stop()
            if random.random() <= 0.06:
                self.kill()

    def stop(self):
        self.speed = 0
    def update(self,psec):
        if self.rect.center != self.destination:
            vec_to_destination = self.destination - self.rect.center
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, self.speed)
            self.rect.center += travel_distance * heading
        elif (self.rect.center == self.destination):
            self.image = self.image2
            self.stop()
            if random.random() <= 0.06:
                self.kill()

        if self.rect.x >= 2000 or self.rect.x <= 0:
            self.kill()
        if self.rect.y>= 1000 or self.rect.y <= 0:
            self.kill()