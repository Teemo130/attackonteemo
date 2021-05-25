import pygame as py
from sys import exit

import pygame.mixer
from pygame.locals import *

def Finishscreen3(start = False):
    pygame.mixer.init()
    sound = py.mixer.Sound('ka-ching.mp3')
    sound.play()
    you_win = "You win!"
    my_font = py.font.SysFont("arial", 100)
    my_font2 = py.font.SysFont("arial", 50)
    backtomanu = "Thank you for playing!"
    title = "ATTACK ON TEEMO"
    my_font2 = py.font.SysFont("arial", 100)
    name_surface1 = my_font2.render(title, True, (0, 0, 0), (255, 255, 255))
    py.image.save(name_surface1, "title.png")
    vict = my_font.render(you_win, True, (255, 0, 0), (255, 255, 255))
    bex = my_font2.render(backtomanu, True, (255, 0, 0), (255, 255, 255))
    py.image.save(vict, "victory.png")
    py.image.save(bex, "bex.png")
    title_pic = py.image.load('title.png').convert_alpha()
    vict_pic = py.image.load("victory.png").convert_alpha()
    next_pic = py.image.load("bex.png").convert_alpha()
    screen = py.display.set_mode((1800, 900), 0, 32)
    while start == True:

        screen.fill((255, 255, 255))

        screen.blit(vict_pic,(600,400))
        screen.blit(title_pic, (500, 100))
        screen.blit(next_pic,(400,600))
        nextlevelbutton = py.Rect(800, 600, 987, 700)
        py.mouse.set_visible(True)
        ponter = py.mouse.get_pos()
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if nextlevelbutton.collidepoint(ponter):
                    return False
        py.display.update()