from boss_stage import Boss_screen
import pygame
from stage10 import stage1screen
from stage import MenuScreen


narro_page = [pygame.image.load("narro_1.png"),pygame.image.load("narro_2.png"),pygame.image.load("narro_3.png"),
               pygame.image.load("narro_4.png"),pygame.image.load("narro_5.png"),pygame.image.load("narro_6.jpg"),
               pygame.image.load("narro_7.png"),pygame.image.load("narro_8.png"),pygame.image.load("narro_9.png"),
               pygame.image.load("narro_10.png"),pygame.image.load("narro_11.png"),pygame.image.load("narro_fin.png")]

narro_screen = MenuScreen('Attack On Teemo')
start_button = pygame.Rect(1600, 800, 1750, 870)
font = pygame.font.SysFont("arial", 64)
def narrow_screen(num):
    @narro_screen.init
    def init_behavior():
        narro_screen.get_window().blit(narro_page[num], (100, 100))
        start = font.render('Start', True, (255, 0, 0))
        narro_screen.get_window().blit(start, (1600, 800))
    init_behavior()

    @narro_screen.update
    def update_behavior():
        start_button = pygame.Rect(1600, 800, 1750, 870)
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        if num<10 and mouse_press[0] and start_button.collidepoint(mouse_pos):
            #load screen
            stage1screen(num,True)
        if num == 10:
            Boss_screen(num, True)
        pygame.display.update()
    update_behavior()