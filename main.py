import os, pygame, socket, threading, random
from pygame.locals import QUIT
from client import Client
import Gui

if __name__ == '__main__': 
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('./sound/kv-beach.mp3')
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()

    address = input("Address :")
    port = input("Port :")

    background = Gui.BG()
    Screen = background.screen #back scrren control to main

    RockClicked = False 
    PaperClicked = False 
    ScissorClicked = False#判斷按鈕是否被按下，預設為否
    StartClicked = False

    player1 = Gui.Player1()
    player2 = Gui.Player2() 
    button = Gui.Button()

    Pc = Client(address, int(port))
    connect = threading.Thread(target = Pc.connect) #Start client do connect
    connect.start()

    done = True
    Punch = "None"

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

        #print(Pc.recvdata["Stage"])

        if Pc.recvdata["Stage"] != None:
            if Pc.recvdata["Stage"] == "WaitP2":
                background.WaitP2()
                background.DoConnect()
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["P2Stage"] != "JoinP2" or Pc.recvdata["Stage"] == "WaitP2_button":
                if Pc.recvdata["Stage"] == "WaitP2_button":
                    background.P2Join()
                    background.DoCheck()
                else:
                    background.P2Join()
                    background.DoGame()
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["P2Stage"] == "JoinP2":
                background.WaitingPuch()
                background.Ready()

                #print(Punch)
                
                if Punch == "None":
                    player1.unknown()
                player2.unknown()

                if Punch == "Rock":
                    player1.Rock()
                if Punch == "Scissors":
                    player1.Scissor()
                if Punch == "Paper":
                    player1.Paper()

            if Pc.recvdata['Stage'] == "Rulest":
                background.again()

                if Pc.recvdata['Ans'] == 'win':
                    background.win()
                if Pc.recvdata['Ans'] == 'loss':
                    background.loss()
                if Pc.recvdata['Ans'] == 'darw':
                    background.darw()

                player1.chiose(Pc.recvdata['Punch'])
                player2.chiose(Pc.recvdata['P2Stage'])
                    



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
            if Pc.recvdata["Stage"] == "WaitP2":
                Pc.data["Stage"] = "Connect" # Go to next stage
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["Stage"] != "WaitP2_button":
                Pc.data["Stage"] = "Start" # Go to next stage
            if Pc.recvdata['Stage'] == "Rulest":
                Pc.recvdata['Punch'] = ''
                Pc.recvdata['Ans'] = None
                Pc.recvdata['P2Stage'] = None
                Pc.recvdata['Stage'] = "WaitP2"
                Pc.data = {"Role":"Client", "Stage":"Connect", "Punch":None}
                Punch = "None"

        if RockClicked:
            button.ButtonRockClick()#如果按下按鈕顯示已按下
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["P2Stage"] == "JoinP2":
                Pc.data["Stage"] = "Punch"
                Punch = "Rock"
                Pc.data["Punch"] = Punch

        if PaperClicked:
            button.ButtonPaperClick()
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["P2Stage"] == "JoinP2":
                Pc.data["Stage"] = "Punch"
                Punch = "Paper"
                Pc.data["Punch"] = Punch

        if ScissorClicked:
            button.ButtonScissorClick()
            button.button_sound.play()
            pygame.display.flip()
            pygame.time.delay(150)
            if Pc.recvdata["Stage"] == "JoinP2" and Pc.recvdata["P2Stage"] == "JoinP2":
                Pc.data["Stage"] = "Punch"
                Punch = "Scissors"
                Pc.data["Punch"] = Punch

            
        PaperClicked = False
        ScissorClicked = False
        RockClicked = False#重新將按鈕設定為未按下
        StartClicked = False#重新將按鈕設定為未按下

        pygame.display.flip()
        clock.tick(30)