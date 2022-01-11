

def RPSgame():
    ServerPlayer = int(input("Input :"))
    ClientPlayer = int(input("Input :"))

    #Check draw
    if ServerPlayer == ClientPlayer:
        print("Draw")
        return {'ServerPlayer': 'darw', 'ClientPlayer': 'darw'}

    elif ServerPlayer == 0 and ClientPlayer == 1:
        print("ServerPlayer input : Scissors") 
        print("ServerPlayer input : Rock") 
        return {'ServerPlayer': 'loss', 'ClientPlayer': 'win'}

    elif ServerPlayer == 0 and ClientPlayer == 2:
        print("ServerPlayer input : Scissors") 
        print("ClientPlayer input : Paper") 
        return {'ServerPlayer': 'win', 'ClientPlayer': 'loss'}

    elif ServerPlayer == 1 and ClientPlayer == 0:
        print("ServerPlayer input : Rock") 
        print("ClientPlayer input : Scissors") 
        return {'ServerPlayer': 'win', 'ClientPlayer': 'loss'}

    elif ServerPlayer == 1 and ClientPlayer == 2:
        print("ServerPlayer input : Rock") 
        print("ClientPlayer input : Paper") 
        return {'ServerPlayer': 'loss', 'ClientPlayer': 'win'}

    elif ServerPlayer == 2 and ClientPlayer == 0:
        print("ServerPlayer input : Paper") 
        print("ClientPlayer input : Scissors") 
        return {'ServerPlayer': 'loss', 'ClientPlayer': 'win'} 

    elif ServerPlayer == 2 and ClientPlayer == 1:
        print("ServerPlayer input : Paper") 
        print("ClientPlayer input : Rock") 
        return {'ServerPlayer': 'win', 'ClientPlayer': 'loss'}

    else:
        print("Error!In function game")
