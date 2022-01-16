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

class Button(Player1):
    def __init__(self):
        super().__init__()
        self.Button_ken = pygame.transform.flip(self.img1, True, False)
        self.Button_pon = pygame.transform.flip(self.img2, True, False)
        self.Button_jan = pygame.transform.flip(self.img3, True, False)
    def ButtonRock(self):
        self.screen.blit(self.Button_ken, (100, 350))
    def ButtonPaper(self):
        self.screen.blit(self.Button_pon, (100, 200))
    def ButtonScissor(self):
        self.screen.blit(self.Button_jan, (100, 50))

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
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('./sound/kv-beach.mp3')
    pygame.mixer.music.play()
    button_sound = pygame.mixer.Sound('./sound/bottle.wav')
    clock = pygame.time.Clock()

    background = BG()
    screen = background.screen #back scrren control to main

    button_clicked = False#判斷按鈕是否被按下，預設為否

    palyer1 = Player1()
    palyer2 = Player2() 
    button = Button()

    inputtext = pygame.image.load('./imgs/Rock.png')
    inputtext_clicked = pygame.image.load('./imgs/Paper.png')
    text = pygame.transform.scale2x(inputtext)
    text_clicked = pygame.transform.scale2x(inputtext_clicked)
    text_rect = screen.blit(text, (300, 300))

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:#當發生左鍵按下的事件
                button_clicked = True if text_rect.collidepoint(event.pos) else False #collidepoint判斷是否重疊

        background.background()
        palyer1.unknown()
        palyer2.unknown()
        button.ButtonRock()
        button.ButtonPaper()
        button.ButtonScissor()

        if button_clicked:
            screen.blit(text_clicked, text_rect)#如果按下按鈕顯示已按下
            button_sound.play()
            pygame.display.flip()
            pygame.time.delay(100)
        else:
            screen.blit(text, text_rect)#否則顯示"button"
        button_clicked = False#重新將按鈕設定為未按下


        pygame.display.flip()
        clock.tick(30)