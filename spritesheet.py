import pygame as py
from pygame.loacl import *
import json
class Spritesheet:
    def __init__(self, file):
        self.file = file
        self.sheet = py.image.load(file)
        self.sheet.convert_alpha()
        self.meta_data = self.file.replace('png','json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()


    def get_sprite(self,x,y,w,h):
        sprite = py.Surface(x,y)
        sprite.blit(self.sheet,(0,0),(x,y,w,h))
        return sprite

    def parse_sprite(self,name):
        sprite = self.data['frame'][name]['frame']
        x,y,w,h = sprite["x"],sprite["y"],sprite["w"],sprite["h"]
        image = self.get_sprite(x,y,w,h)
        return image