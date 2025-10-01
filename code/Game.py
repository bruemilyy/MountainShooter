import pygame as pg
from code.Menu import Menu
class Game:
    def _init_(self):
        pg.init()
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #Check for all events
            #for event in pg.event.get():
                #if event.type == pg.QUIT:
                    #pg.quit() #Close window
                    #quit() #End pygame