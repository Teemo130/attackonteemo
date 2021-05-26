import pygame
import sys


class Screen:
    """
    A base class to represent a screen, not meant to be directly instantiated

    ...

    Attributes
    ----------
    window: pygame.display
        base window for the screen

    caption: str
        title of the window

    Methods
    -------
    None
    """

    def __init__(self, caption):
        """
        parameters
        ----------
        caption: str
            title  of the window
        """
        pygame.init()
        self.window = pygame.display.set_mode((1800, 900))
        self.caption = caption
        pygame.display.set_caption(caption)


class LevelScreen(Screen):
    """
    a class for an object to represent a window for gameplay

    ...

    Attributes
    ----------
    clock: pygame.time.Clock
        a clock to measure game time

    Methods
    -------
    update(func: func):
        controls what the screen is displaying
    """

    def __init(self, caption):
        """
        parameters
        ----------
        caption: str
            title of the window
        """
        super().__init__(caption)
        self.clock = pygame.time.Clock()

    def update(self, func):
        """
        Designed to be used as decorator. Functions with this decorator activate the basic game loop behavior and
        controls what the window is displaying.

        parameters:
            func: func:
                a function that defines the behavior of the window
        """

        def wrapper(*args, **kwargs):
            while True:
                self.clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                func(*args, **kwargs)
                pygame.display.update()


class MenuScreen(Screen):
    """
    A class for an object to represent a window for menus and gui's

    Attributes
    ----------
        None

    Methods
    -------
    update(func: func):
        controls what the screen is displaying
    """
    def __init__(self, caption):
        """
        Designed to be used as a decorator. Functions with this decorator activate the window and control what it
        is displaying

        parameters:
            func: func:
                a function that defines the behavior of the window
        """
        super().__init__(caption)

    @staticmethod
    def update(func):
        def wrapper(*args, **kwargs):
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                func(*args, **kwargs)
                pygame.display.update()
        return wrapper


def go():
    """Example of how to use the update decorator"""

    screen = MenuScreen('Test Screen')

    @screen.update
    def behavior():
        print('hello')
    behavior()


if __name__ == '__main__':
    go()
