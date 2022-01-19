from multiprocessing.connection import wait
import os, pygame, socket, threading, random
from pygame.locals import QUIT
from game import RPSgame
from client import Client

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
        self.font = pygame.font.SysFont('Comic Sans MS', 50, bold = True, italic = True)
        self.sfont = pygame.font.SysFont('Comic Sans MS', 25, bold = True, italic = True)
        self.period = 0

    def background(self):
        self.screen.blit(self.bg, (0, 0))

    def WaitingP2(self):
        if self.period > 3:
            self.period = 0
        text = 'Waiting player2' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        screen.blit(textsurface,(390, 25))

    def P2Join(self):
        if self.period > 3:
            self.period = 0
        text = 'Player2 Join Game' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        screen.blit(textsurface,(390, 25))

    def Startgame(self):
        text = 'Start Game'
        if pygame.time.get_ticks() % 30 == 0:
            textsurface = self.sfont.render(text, False, (255, 128, 114))
            screen.blit(textsurface,(960, 150))
        else:
            textsurface = self.sfont.render(text, False, (255, 0, 0))
            screen.blit(textsurface,(960, 150))

    def P2Startgame(self):
        text = 'P2 Ready'
        if pygame.time.get_ticks() % 30 == 0:
            textsurface = self.sfont.render(text, False, (255, 128, 114))
            screen.blit(textsurface,(975, 150))
        else:
            textsurface = self.sfont.render(text, False, (255, 0, 0))
            screen.blit(textsurface,(975, 150))

    def WaitingPuch(self):
        if self.period > 3:
            self.period = 0
        text = 'throw' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        screen.blit(textsurface,(500, 25))

class Player1(BG):
    def __init__(self):
        super().__init__()
        self.Stage = None
        self.player1_ken = pygame.transform.flip(self.chiose_ken, True, False)
        self.player1_pon = pygame.transform.flip(self.chiose_pon, True, False)
        self.player1_jan = pygame.transform.flip(self.chiose_jan, True, False)
        self.x = 320
        self.y = 150

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
        """
        if self.state == "Rock":
            self.Rock()
        if self.state == "Scissors":
            self.Paper()
        if self.state == "Paper":
            self.Scissor()
        if self.state == None:
            pass
        """

class Player2(BG):
    def __init__(self):
        super().__init__()
        self.Stage = None
        self.x = 630
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
        self.Button_start = pygame.image.load('./imgs/Start_gb.png')
        self.Button_ken = pygame.image.load('./imgs/Rock_gb.png')
        self.Button_pon = pygame.image.load('./imgs/Paper_gb.png')
        self.Button_jan = pygame.image.load('./imgs/Scissors_gb.png')
        self.Button_start_click = pygame.image.load('./imgs/Start_yb.png')
        self.Button_ken_click = pygame.image.load('./imgs/Rock_yb.png')
        self.Button_pon_click = pygame.image.load('./imgs/Paper_yb.png')
        self.Button_jan_click = pygame.image.load('./imgs/Scissors_yb.png')
    def ButtonStart(self):
        self.start_rect = self.screen.blit(self.Button_start, (920, 200))
    def ButtonStartClick(self):
        self.start_rect = self.screen.blit(self.Button_start_click, (920, 200))
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
    StartClicked = False

    player1 = Player1()
    player2 = Player2() 
    button = Button()

    Pc = Client("127.0.0.1", 1060)
    connect = threading.Thread(target = Pc.connect) #Start client do connect
    connect.start()

    done = True
    while done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                os._exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:#當發生左鍵按下的事件
                StartClicked = True if StartRect.collidepoint(event.pos) else False
                RockClicked = True if RockRect.collidepoint(event.pos) else False #collidepoint判斷是否重疊
                PaperClicked = True if PaperRect.collidepoint(event.pos) else False 
                ScissorClicked = True if ScissorRect.collidepoint(event.pos) else False

        background.background()

        print(Pc.recvdata)

        if Pc.recvdata["Stage"] == "WaitP2" or Pc.recvdata["Stage"] == "P2Join":

            if Pc.recvdata["Stage"] == "WaitP2":
                background.WaitingP2()

            if Pc.recvdata["Stage"] == "P2Join": #waiting start
                background.P2Join()
                if Pc.recvdata["P2Stage"] == "P2WaitPunch":
                    background.P2Startgame()
                else:
                    background.Startgame()

            button.ButtonRock() #buttons rect
            RockRect = button.rock_rect
            button.ButtonPaper()
            PaperRect = button.paper_rect
            button.ButtonScissor()
            ScissorRect = button.scissor_rect
            button.ButtonStart()
            StartRect = button.start_rect

            if StartClicked:
                button.ButtonStartClick()#如果按下按鈕顯示已按下
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)
                if Pc.recvdata["Stage"] == "P2Join":
                        Pc.data["GameStage"] = "WaitPunch" # Go to next stage

            if RockClicked:
                button.ButtonRockClick()#如果按下按鈕顯示已按下
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)

            if PaperClicked:
                button.ButtonPaperClick()
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)

            if ScissorClicked:
                button.ButtonScissorClick()
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)
                
            PaperClicked = False
            ScissorClicked = False
            RockClicked = False#重新將按鈕設定為未按下
            StartClicked = False#重新將按鈕設定為未按下


        if Pc.recvdata["Stage"] == "WaitPunch": #waiting punch
            background.WaitingPuch()

            button.ButtonRock() #buttons rect
            button.ButtonPaper()
            button.ButtonScissor()
            button.ButtonStart()

            if StartClicked:
                button.ButtonStartClick()#如果按下按鈕顯示已按下
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)

            if RockClicked:
                button.ButtonRockClick()#如果按下按鈕顯示已按下
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)

            if PaperClicked:
                button.ButtonPaperClick()
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)

            if ScissorClicked:
                button.ButtonScissorClick()
                button.button_sound.play()
                pygame.display.flip()
                pygame.time.delay(150)
                
            PaperClicked = False
            ScissorClicked = False
            RockClicked = False#重新將按鈕設定為未按下
            StartClicked = False#重新將按鈕設定為未按下

        pygame.display.flip()
        clock.tick(30)