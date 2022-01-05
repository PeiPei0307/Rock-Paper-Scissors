import os, pygame, socket, threading
from pygame.locals import QUIT
from game import RPSgame
from server import Server
from client import Client

quit = False
role = None

def background(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Rock-Paper-Scissors!')
    bg = pygame.image.load('./imgs/Bg.jpg')
    screen.blit(bg, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)

if __name__ == '__main__': 

    choices = {'client': Client, 'server': Server} #Back-end connection test
    role = choices[input(">>>")]()
    role.start()
    
    pygame.init() #Front-end building
    Bg = threading.Thread(target = background, args = (1200, 650))
    Bg.start()
    
    #RPSgame()