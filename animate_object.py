import pygame
from PIL import Image, ImageSequence


class Animate(pygame.sprite.Sprite):
    def __init__(self,  images):
        pygame.sprite.Sprite.__init__(self)
        self.leftImages = images
        self.images = self.leftImages
        self.image = self.images[0]
        self.mask = self.image.get_masks()
        self.image_index = 0
        self.walking = True

    def update(self):
        if self.walking:
            self.image = self.images[self.image_index % len(self.images)]

    def loadGIF(self, filename):
        self.pilImage = Image.open(filename)
        frames = []
        for frame in ImageSequence.Iterator(self.pilImage):
            frame = frame.convert('RGBA')
            pygameImage = pygame.image.fromstring(
                frame.tobytes(), frame.size, frame.mode).convert_alpha()
            frames.append(pygameImage)
        return frames

