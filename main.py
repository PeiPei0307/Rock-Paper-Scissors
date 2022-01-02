import sys, pygame, socket, threading
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

def Server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 5000))
    sock.listen(1)
    print('Listening at', sock.getsockname())
    while True:
        print('Waiting to accept a new connection')
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        sc.close()
        print('  Reply sent, socket closed')

def Client():
    host = '127.0.0.1'
    port = 5000
    #host, port = input("Input server address!").split(' ')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    print('Client has been assigned socket name', sock.getsockname())
    sock.close()

if __name__ == '__main__': 

    choices = {'client': Client, 'server': Server} #Back-end connection test
    role = input(">>>")
    function = choices[role]
    start = threading.Thread(target = function)
    start.start()
    
    pygame.init() #Front-end building
    game = background()
    game.start()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                start.join()
                pygame.quit()
                sys.exit()