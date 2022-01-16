import os, pygame, socket, threading, random
from pygame.locals import QUIT
from game import RPSgame
from server import Server
from client import Client

quit = False
role = None

class BG():

    def __init__(self):
        self.width = 1200
        self.height = 650
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Rock-Paper-Scissors!')
        self.bg = pygame.image.load('./imgs/Bg.jpg')
        self.img1 = pygame.image.load('./imgs/Rock.png')
        self.img2 = pygame.image.load('./imgs/Paper.png')
        self.img3 = pygame.image.load('./imgs/Scissors.png')
        self.img4 = pygame.image.load('./imgs/question/null.png')
        self.chiose_ken = pygame.transform.scale2x(self.img1)
        self.chiose_pon = pygame.transform.scale2x(self.img2)
        self.chiose_jan = pygame.transform.scale2x(self.img3)

    def background(self):
        self.screen.blit(self.bg, (0, 0))

class Player1(BG):
    def __init__(self):
        super().__init__()
        self.player1_ken = pygame.transform.flip(self.chiose_ken, True, False)
        self.player1_pon = pygame.transform.flip(self.chiose_pon, True, False)
        self.player1_jan = pygame.transform.flip(self.chiose_jan, True, False)
        self.x = 300
        self.y = 100

    def Rock(self):
        self.screen.blit(self.player1_ken, (self.x, self.y))
    def Paper(self):
        self.screen.blit(self.player1_pon, (self.x, self.y))
    def Scissor(self):
        self.screen.blit(self.player1_jan, (self.x, self.y))

    def unknown(self):
        test = random.randint(1,3)
        if test == 1:
            self.Rock()
        if test == 2:
            self.Paper()
        if test == 3:
            self.Scissor()

class Player2(BG):
    def __init__(self):
        super().__init__()
        self.x = 650
        self.y = 100

    def Rock(self):
        self.screen.blit(self.chiose_ken, (self.x, self.y))
    def Paper(self):
        self.screen.blit(self.chiose_pon, (self.x, self.y))
    def Scissor(self):
        self.screen.blit(self.chiose_jan, (self.x, self.y))

    def unknown(self):
        test = random.randint(1,3)
        if test == 1:
            self.Rock()
        if test == 2:
            self.Paper()
        if test == 3:
            self.Scissor()



"""
class Player1:
    def __init__(self):
        threading.Thread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5000
"""

if __name__ == '__main__': 

    clock = pygame.time.Clock()

    back = BG()
    back.background()

    palyer1 = Player1()
    palyer2 = Player2() 

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

        back.background()
        palyer1.unknown()
        palyer2.unknown()


        pygame.display.flip()
        clock.tick(30)