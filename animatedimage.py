import pygame
import spritesheet as tsss

from PIL import Image, ImageSequence

sprite_sheet_file = "spelunky-oc-sprite-sheet.png"


def loadGIF(filename):

    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()
        frames.append(pygameImage)


    sequence = tsss.AnimationSequence({ "image": frames })
    return sequence

class AnimatedSpriteObject(pygame.sprite.Sprite):

    def __init__(self, x, bottom, animSequence):
        pygame.sprite.Sprite.__init__(self)
        self.animSequence = animSequence
        self.animSequence.start("left")
        self.walkingLeft = True
        self.image = self.animSequence.get_frame(0)
        self.rect = self.image.get_rect(midbottom = (x, bottom + 10))

    def update(self):
        if self.walkingLeft:
            self.image = self.animSequence.get_frame(0.2)
            self.rect.x -= 10
            if self.rect.right < 0:
                """turn around and go the other way"""
                self.walkingLeft = False
                self.animSequence.start("right")
                self.image = self.animSequence.get_frame(0.0)
        else:
            self.image = self.animSequence.get_frame(0.05)
            self.rect.x += 5
            if self.rect.left > pygame.display.get_surface().get_width():
                """turn around and go the other way"""
                self.walkingLeft = True
                self.animSequence.start("left")
                self.image = self.animSequence.get_frame(0.0)