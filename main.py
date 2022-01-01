import sys, pygame, threading
from pygame.locals import QUIT

class background:
    def __init__(self, W = 1200, H = 650):
        self.width = W
        self.height = H
    def start(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')
        bg = pygame.image.load('./imgs/Bg.jpg')
        self.screen.blit(bg, (0, 0))
        pygame.display.update()

if __name__ == '__main__': 
    
    pygame.init()
    game = background()
    game.start()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()