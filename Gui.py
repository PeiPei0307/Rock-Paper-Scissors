import pygame, random

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

    def WaitP2(self):
        if self.period > 3:
            self.period = 0
        text = 'Waiting player2' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(390, 25))

    def DoConnect(self):
        text = 'Connect'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(980, 150))

    def P2Join(self):
        if self.period > 3:
            self.period = 0
        text = 'Player2 Join Game' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(390, 25))

    def DoCheck(self):
        text = 'Waiting P2 Check'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(920, 150))

    def DoGame(self):
        text = 'Start Game'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(960, 150))

    def WaitingPuch(self):
        if self.period > 3:
            self.period = 0
        text = 'throw' + '.' * self.period
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def Ready(self):
        text = 'Ready'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(985, 150))

    def win(self):
        text = "Win!!!"
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def loss(self):
        text = "Lose..."
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def darw(self):
        text = "Darw"
        self.period += 1
        textsurface = self.font.render(text, False, (240, 85, 85))
        self.screen.blit(textsurface,(500, 25))

    def again(self):
        text = 'Again'
        textsurface = self.sfont.render(text, False, (255, 0, 0))
        self.screen.blit(textsurface,(985, 150))

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

    def chiose(self, i):
        if i == "Rock":
            self.Rock()
        if i == "Paper":
            self.Paper()
        if i == "Scissors":
            self.Scissor()
        if i == None:
            pass

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

    def chiose(self, i):
        if i == "Rock":
            self.Rock()
        if i == "Paper":
            self.Paper()
        if i == "Scissors":
            self.Scissor()
        if i == None:
            pass

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