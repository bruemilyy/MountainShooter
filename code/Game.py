import pygame
from code.Menu import Menu
from code.Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def _init_(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

