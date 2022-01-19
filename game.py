

def RPSgame(Play1, Play2):
    Player1 = Play1
    Player2 = Play2

    #print(Player1)
    #print(Player2)

    #Check
    if Player1 == Player2:
        print("Draw")
        return {'Player1': 'darw', 'Player2': 'darw'}

    elif Player1 == "Scissors" and Player2 == "Rock":
        print("Player1 input : Scissors") 
        print("Player2 input : Rock") 
        return {'Player1': 'loss', 'Player2': 'win'}

    elif Player1 == "Scissors" and Player2 == "Paper":
        print("Player1 input : Scissors") 
        print("Player2 input : Paper") 
        return {'Player1': 'win', 'Player2': 'loss'}

    elif Player1 == "Rock" and Player2 == "Scissors":
        print("Player1 input : Rock") 
        print("Player2 input : Scissors") 
        return {'Player1': 'win', 'Player2': 'loss'}

    elif Player1 == "Rock" and Player2 == "Paper":
        print("Player1 input : Rock") 
        print("Player2 input : Paper") 
        return {'Player1': 'loss', 'Player2': 'win'}

    elif Player1 == "Paper" and Player2 == "Scissors":
        print("Player1 input : Paper") 
        print("Player2 input : Scissors") 
        return {'Player1': 'loss', 'Player2': 'win'} 

    elif Player1 == "Paper" and Player2 == "Rock":
        print("Player1 input : Paper") 
        print("Player2 input : Rock") 
        return {'Player1': 'win', 'Player2': 'loss'}

    else:
        print("Error!In function game")