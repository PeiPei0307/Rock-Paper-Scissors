# __author__=="thomas"
import pygame
pygame.init()
screen = pygame.display.set_mode((1200, 650))
pygame.display.set_caption("顯示圖片")
# 設置背景顏色
screen.fill((255, 255, 255))
# ============遊戲開始頁面靜態效果==========
#1.載入圖片
bg = pygame.image.load('./imgs/Bg.jpg')
img3 = pygame.image.load('./imgs/Scissors.png') #橘色随便改路径#1是剪刀2是石头3是布
img2 = pygame.image.load('./imgs/Rock.png')
img1 = pygame.image.load('./imgs/Paper.png') 


#2.圖片位置
#blit(渲染對象，座標)
screen.blit(bg, (0, 0))
screen.blit(img3, (100, 250))
screen.blit(img2, (400, 250))
screen.blit(img1, (700, 250))
#刷新顯示頁面
#1.第一次刷新用它 pygame.display.flip()
#2.不是第一次刷新
pygame.display.update() #刷新
flag = True
while flag:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()
