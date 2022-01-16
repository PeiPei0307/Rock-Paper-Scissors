# coding: utf-8
import pygame
import time


def main():
    # Settings
    width = 800
    height = 600
    color_bg = (255, 255, 0)#顏色亮度參數(紅色,綠色,藍色)
    color_text = (255, 255, 255)#顏色亮度參數(紅色,綠色,藍色)
    button_clicked = False#判斷按鈕是否被按下，預設為否
    running = True

    # Init
    pygame.init()
    screen = pygame.display.set_mode((width, height))#視窗長寬
    pygame.display.set_caption("Rect Demo")#視窗名稱

    # Text
    font = pygame.font.SysFont("Arial", 35)#(字形/*可不填*/, 大小)

    inputtext = pygame.image.load('./imgs/Rock.png')
    inputtext_clicked = pygame.image.load('./imgs/Paper.png')
    text = pygame.transform.scale2x(inputtext)
    text_clicked = pygame.transform.scale2x(inputtext_clicked)
    text_rect = text.get_rect(center=(width/2, height/2))

    # 開始跑程式迴圈
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#按下視窗的X關閉視窗
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:#當發生左鍵按下的事件
                button_clicked = True if text_rect.collidepoint(event.pos) else False #collidepoint判斷是否重疊

        # Screen
        screen.fill(color_bg)#背景填色

        # Draw
        pygame.draw.rect(screen, (100, 100, 100), text_rect)#(繪製平面, 顏色, ? , 線寬/*0為填滿*/)

        if button_clicked:
            screen.blit(text_clicked, text_rect)#如果按下按鈕顯示已按下
        else:
            screen.blit(text, text_rect)#否則顯示"button"

        # Updates
        
        pygame.display.update()#更新畫面
        button_clicked = False#重新將按鈕設定為未按下
        time.sleep(0.2)#停頓0.2秒 記得import time

if __name__ == "__main__":
    main()
