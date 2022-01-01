import sys, pygame, threading
from pygame.locals import QUIT

class Screen:
    def __init__(self, W, H):
        self.width = W
        self.height = H
    
    def background(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')
        self.screen.fill((255, 255, 255))
        #bg = pygame.image.load('./imgs/Bg.jpg')
        #self.screen.blit(bg, (0, 0))
        pygame.display.update()

    def Input_text(self, text):
        self.Input = text
        self.screen.fill((255, 255, 255))
        self.head_font = pygame.font.SysFont(None, 60)
        self.text_surface = self.head_font.render('start', True, (0, 0, 0))
        self.screen.blit(self.text_surface, (10, 10))
        pygame.display.update()



if __name__ == '__main__': 
    pygame.init()

    game = Screen(1200, 650)
    game.background()

    while True:
        input

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()