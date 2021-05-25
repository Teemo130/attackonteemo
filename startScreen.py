
import pygame
from stage1 import stage1screen
from sys import exit
from pygame.locals import *

def startscreen():
    pygame.init()
    pygame.display.set_caption("Attack On Teemo")
    screen = pygame.display.set_mode((1800, 900), 0, 32)
    screen.fill((255, 255, 255))
    start = "START"
    my_font = pygame.font.SysFont("arial", 60)
    my_font.set_bold(True)
    name_surface = my_font.render(start, True, (255, 0, 0), (255, 255, 255))
    pygame.image.save(name_surface, "start.png")
    title = "ATTACK ON TEEMO"
    my_font2 = pygame.font.SysFont("arial", 100)
    name_surface1 = my_font2.render(title, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(name_surface1, "title.png")
    teemopic = pygame.image.load("teemo.png").convert_alpha()
    teemopic2 = pygame.transform.flip(teemopic, True, False)
    start_pic = pygame.image.load('start.png').convert_alpha()
    title_pic = pygame.image.load('title.png').convert_alpha()
    while True:

        start_rect = start_pic.get_rect()
        screen.blit(start_pic,(800,450))
        screen.blit(title_pic,(500,100))
        screen.blit(teemopic,(150,100))
        screen.blit(teemopic2, (1500, 100))

        ponter = pygame.mouse.get_pos()
        x, y = pygame.mouse.get_pos()
        startbutton = pygame.Rect(800, 450, 987, 519)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if startbutton.collidepoint(ponter):
                    stage1screen(1, start = True)
        pygame.display.update()

startscreen()