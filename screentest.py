import os, pygame, socket, threading, random
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
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')

        self.bg = pygame.image.load('./imgs/Bg.jpg')
        self.img1 = pygame.image.load('./imgs/Rock.png')
        self.img2 = pygame.image.load('./imgs/Paper.png')
        self.img3 = pygame.image.load('./imgs/Scissors.png')
        self.img4 = pygame.image.load('./imgs/question/null.png')

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def Rock(self):
        self.screen.blit(self.img1, (100, 250))

    def Paper(self):
        self.screen.blit(self.img2, (100, 250))

    def Scissor(self):
        self.screen.blit(self.img3, (100, 250))

    def null(self):
        self.screen.blit(self.img4, (100, 250))


class Player1:
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5000

if __name__ == '__main__': 

    clock = pygame.time.Clock()

    back = BG(1200, 650)
    back.background()

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = False

        back.background()

        test = random.randint(1,3)
        if test == 1:
            back.Scissor()
        if test == 2:
            back.Rock()
        if test == 3:
            back.Paper()

        pygame.display.flip()
        clock.tick(15)
    pygame.quit()