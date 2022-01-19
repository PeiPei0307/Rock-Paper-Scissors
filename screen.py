import os, pygame, socket, threading, random
from pygame.locals import QUIT
from game import RPSgame
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
        self.state = None
        self.player1_ken = pygame.transform.flip(self.chiose_ken, True, False)
        self.player1_pon = pygame.transform.flip(self.chiose_pon, True, False)
        self.player1_jan = pygame.transform.flip(self.chiose_jan, True, False)
        self.x = 300
        self.y = 150

    def Rock(self):
        self.screen.blit(self.player1_ken, (self.x, self.y))
    def Paper(self):
        self.screen.blit(self.player1_pon, (self.x, self.y))
    def Scissor(self):
        self.screen.blit(self.player1_jan, (self.x, self.y))

    def Chiose(self):
        if self.state == "Rock":
            self.Rock()
        if self.state == "Scissors":
            self.Paper()
        if self.state == "Paper":
            self.Scissor()
        if self.state == None:
            pass

class Player2(BG):
    def __init__(self):
        super().__init__()
        self.state = None
        self.x = 650
        self.y = 150

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

class Button(Player1):
    def __init__(self):
        super().__init__()
        self.button_sound = pygame.mixer.Sound('./sound/bottle.wav')
        self.Button_ken = pygame.image.load('./imgs/Rock_gb.png')
        self.Button_pon = pygame.image.load('./imgs/Paper_gb.png')
        self.Button_jan = pygame.image.load('./imgs/Scissors_gb.png')
        self.Button_ken_click = pygame.image.load('./imgs/Rock_yb.png')
        self.Button_pon_click = pygame.image.load('./imgs/Paper_yb.png')
        self.Button_jan_click = pygame.image.load('./imgs/Scissors_yb.png')
    def ButtonRock(self):
        self.rock_rect = self.screen.blit(self.Button_ken, (100, 350))
    def ButtonRockClick(self):
        self.screen.blit(self.Button_ken_click, (100, 350))
    def ButtonPaper(self):
        self.paper_rect = self.screen.blit(self.Button_pon, (100, 200))
    def ButtonPaperClick(self):
        self.screen.blit(self.Button_pon_click, (100, 200))
    def ButtonScissor(self):
        self.scissor_rect = self.screen.blit(self.Button_jan, (100, 50))
    def ButtonScissorClick(self):
        self.scissor_rect = self.screen.blit(self.Button_jan_click, (100, 50))

if __name__ == '__main__': 
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('./sound/kv-beach.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()

    background = BG()
    screen = background.screen #back scrren control to main

    RockClicked = False 
    PaperClicked = False 
    ScissorClicked = False#判斷按鈕是否被按下，預設為否

    player1 = Player1()
    player2 = Player2() 
    button = Button()

    Pc = Client("127.0.0.1", 1060)
    connect = threading.Thread(target = Pc.connect)
    connect.start()

    """
    if callback["State"] == "Rock":
        palyer1.chiose_ken()
    if callback["State"] == "Scissors":
        palyer1.chiose_jan()
    if callback["State"] == "Paper":
        palyer1.chiose_pon()
    """

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:#當發生左鍵按下的事件
                RockClicked = True if RockRect.collidepoint(event.pos) else False #collidepoint判斷是否重疊
                PaperClicked = True if PaperRect.collidepoint(event.pos) else False #collidepoint判斷是否重疊
                ScissorClicked = True if ScissorRect.collidepoint(event.pos) else False #collidepoint判斷是否重疊

        background.background()

        if Pc.recvdata != None:
            player1.state = Pc.recvdata["State"]

        player1.Chiose()

        button.ButtonRock() #buttons rect
        RockRect = button.rock_rect
        button.ButtonPaper()
        PaperRect = button.paper_rect
        button.ButtonScissor()
        ScissorRect = button.scissor_rect

        if RockClicked:
            button.ButtonRockClick()#如果按下按鈕顯示已按下
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            RockClicked = False#重新將按鈕設定為未按下

        if PaperClicked:
            button.ButtonPaperClick()
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            PaperClicked = False

        if ScissorClicked:
            button.ButtonScissorClick()
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            ScissorClicked = False


        pygame.display.flip()
        clock.tick(15)