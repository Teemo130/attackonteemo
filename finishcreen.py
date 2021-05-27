import pygame as py
from sys import exit
from pygame.locals import *
from stage2screen import stage2screen

def Finishscreen(start = False):
    
    py.init()
    py.mixer.init()
    sound = py.mixer.Sound('ka-ching.mp3')
    sound.play()
    you_win = "You win!"
    my_font = py.font.SysFont("arial", 100)
    my_font2 = py.font.SysFont("arial", 50)
    next = "Next Level"
    title = "ATTACK ON TEEMO"
    my_font2 = py.font.SysFont("arial", 100)
    name_surface1 = my_font2.render(title, True, (0, 0, 0), (255, 255, 255))
    py.image.save(name_surface1, "title.png")
    vict = my_font.render(you_win, True, (255, 0, 0), (255, 255, 255))
    nex = my_font2.render(next, True, (255, 0, 0), (255, 255, 255))
    py.image.save(vict, "victory.png")
    py.image.save(nex, "next.png")

    while start == True:
        screen = py.display.set_mode((1800, 900), 0, 32)
        screen.fill((255, 255, 255))
        title_pic = py.image.load('title.png').convert_alpha()
        vict_pic = py.image.load("victory.png").convert_alpha()
        next_pic = py.image.load("next.png").convert_alpha()
        screen.blit(vict_pic, (600, 400))
        screen.blit(title_pic, (500, 100))
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
                    stage2screen(2,start = True)
                    return False
        py.display.update()



