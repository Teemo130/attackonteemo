import pygame as py
import pygame.sprite
from vector import Vector2
import math

class Canshell(py.sprite.Sprite):
    def __init__(self,image,location, destination, speed):
        super().__init__()
        self.speed = speed
        self.image = image
        self.x = location.rect.x
        self.y = location.rect.y
        self.mask = self.image.get_masks()
        self.rect = self.image.get_rect(center=location.rect.center)
        self.is_dead = False
        self.destination = destination.rect.center
        self.destination_beta = destination.rect.center
        self.destination = Vector2(self.destination)
        if self.rect.center != self.destination:
            vec_to_destination = self.destination - self.rect.center
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, self.speed)
            self.rect.center += travel_distance * heading
        self.rotate()

    def rotate(self):
        rel_x, rel_y = self.destination_beta
        rel_x -= self.x
        rel_y -= self.y
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        self.image = py.transform.rotozoom(self.image, angle*1.7, 1)

    def collide(self,othergroup):
        pygame.sprite.spritecollide(self, othergroup, False)
        self.is_dead = True

    def update(self,psec):
        if self.rect.center != self.destination:
            vec_to_destination = self.destination - self.rect.center
            distance_to_destination = vec_to_destination.get_length()
            heading = vec_to_destination.get_normalized()
            travel_distance = min(distance_to_destination, self.speed)
            self.rect.center += travel_distance * heading
        elif (self.rect.center == self.destination) or self.is_dead:
            self.kill()
        if self.rect.x >= 2000 or self.rect.x <= 0:
            self.kill()
        if self.rect.y>= 1000 or self.rect.y <= 0:
            self.kill()