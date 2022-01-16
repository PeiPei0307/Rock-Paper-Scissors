import os, pygame, socket, threading, time
from pygame.locals import QUIT
from game import RPSgame
from server import Server
from client import Client

quit = False
role = None

class BG():

    def __init__(self, W, H):
        self.width = W
        self.height = H

    def background(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')
        self.bg = pygame.image.load('./imgs/Bg.jpg')
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()

    def scissor(self):
        self.img3 = pygame.image.load('./imgs/Scissors.png')
        self.screen.blit(self.img3, (100, 250))
        pygame.display.update()

class Player1:
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5000

if __name__ == '__main__': 
    back = BG(1200, 650)
    back.background()
    time.sleep(1)
    back.scissor()
    time.sleep(1)
    back.background()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)