import pygame as py
from sys import exit
from pygame.locals import *
from narro7 import narrow_screen

win = py.image.load("you_win_level.png")
def Finishscreen(level, start = False):
    level += 1
    py.init()
    py.mixer.init()
    sound = py.mixer.Sound('ka-ching.mp3')
    sound.play()
    next = "Next Level"
    my_font2 = py.font.SysFont("arial", 100)
    nex = my_font2.render(next, True, (255, 0, 0), (255, 255, 255))
    py.image.save(nex, "next.png")

    while start == True:
        screen = py.display.set_mode((1800, 900),py.FULLSCREEN)
        screen.blit(win,(0,0))
        next_pic = py.image.load("next.png").convert_alpha()
        screen.blit(next_pic, (800, 600))
        nextlevelbutton = py.Rect(800, 600, 987, 700)
        py.mouse.set_visible(True)
        ponter = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if nextlevelbutton.collidepoint(ponter):
                    narrow_screen(7)


        py.display.update()