import pygame
from pygame.locals import *

def gameoverscreen(start = False):
    while start == True:
        pygame.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Attack On Teemo")
        screen = pygame.display.set_mode((1800, 900), 0, 32)
        screen.fill((255,255,255))
        start = "please start again"
        my_font = pygame.font.SysFont("arial", 60)
        my_font.set_bold(True)
        name_surface = my_font.render(start, True, (255, 0, 0), (255, 255, 255))
        pygame.image.save(name_surface, "again.png")
        title = "GAME OVER"
        my_font2 = pygame.font.SysFont("arial", 100)
        name_surface1 = my_font2.render(title, True, (0, 0, 0), (255, 255, 255))
        pygame.image.save(name_surface1, "gameover.png")
        teemopic = pygame.image.load("teemo.png").convert_alpha()
        teemopic2 = pygame.transform.flip(teemopic,True,False)
        start_pic = pygame.image.load('again.png').convert_alpha()
        title_pic = pygame.image.load('gameover.png').convert_alpha()
        screen.blit(start_pic,(800,450))
        screen.blit(title_pic,(500,100))
        screen.blit(teemopic,(150,100))
        screen.blit(teemopic2, (1500, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

