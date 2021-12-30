import argparse, random, socket, sys

if __name__ == '__main__':
user1 = int(input("請玩家1輸入：剪刀：（0）、石頭（1）布（2）"))
user2 = int(input("請玩家2輸入：剪刀：（0）、石頭（1）布（2）"))
if user1 == user2:
      if user1 == user2 == 1:
        print("玩家1你輸入的為:剪刀(1)") 
        print("玩家2你輸入的為:剪刀(1)") 
    
      elif user1 == user2 == 1: 
        print("玩家1你輸入的為:石頭(1)") 
        print("玩家2你輸入的為:石頭(1)") 
      elif user1 == user2 == 2: 
        print("玩家1你輸入的為:石頭(2)") 
        print("玩家2你輸入的為:石頭(2)") 
        print("玩家1玩家2平局哩") 
elif user1 == 0 and user2 == 1:
    print("玩家1你的輸入為：剪刀（0）") 
    print("玩家2你的輸入為：石頭 (1)") 
    print("玩家1，你輸給了玩家2")        
    print("玩家2，你贏了玩家1")    
elif user1 == 0 and user2 == 2:
    print("玩家1你的輸入為：剪刀（0）") 
    print("玩家2你的輸入為：布 (2)") 
    print("玩家1，你贏了玩家2")        
    print("玩家2，你輸給玩家1")   
elif user1 == 1 and user2 == 0:
    print("玩家1你的輸入為：石頭（1）") 
    print("玩家2你的輸入為：剪刀 (0)") 
    print("玩家1，你贏了玩家2")        
    print("玩家2，你輸給了玩家1")   
elif user1 == 1 and user2 == 2:
    print("玩家1你的輸入為：石頭（1）") 
    print("玩家2你的輸入為：布 (2)") 
    print("玩家1，你輸給了玩家2")        
    print("玩家2，你贏了玩家1")   
elif user1 == 2 and user2 == 0:
    print("玩家1你的輸入為：布（2）") 
    print("玩家2你的輸入為：剪刀 (0)") 
    print("玩家1，你輸給了玩家2")        
    print("玩家2，你贏了玩家1")  
elif user1 == 2 and user2 == 1:
    print("玩家1你的輸入為：布（2）") 
    print("玩家2你的輸入為：石頭 (1)") 
    print("玩家1，你贏了玩家2")        
    print("玩家2，你輸給玩家1")            
