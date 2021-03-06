from narro import narrow_screen
from stage import *


def startscreen(start = False):
    start_screen = MenuScreen('Attack On Teemo')

    start_screen_image = pygame.image.load('title_screen.png')

    @start_screen.init
    def init_behavior():
        start_screen.get_window().blit(start_screen_image, (0, 0))
    init_behavior()

    @start_screen.update
    def update_behavior():
        mouse_press = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        start_button = pygame.Rect(824, 190, 153, 63)
        if mouse_press[0] and start_button.collidepoint(mouse_pos):
            narrow_screen(0)
    update_behavior()



