import random
print("Welcome to rock, paper, scissors!")

def youLose() :
    print("Sorry, you lose")

def youWin() :
    print("Hooray! You Win!")

def youTied():
    print("It's a tie!")

def printCompMove(move) :
    if(move == 'r') :
        moveName = 'rock'
    elif(move == 'p') :
        moveName = 'paper'
    elif(move == 's'): 
        moveName = 'scissors'
    print(f"Computer's move: {moveName}")

userMove = input("Let's play! Choose rock (r), paper (p), or scissors (s): ")
compMove = random.choice(['r', 'p', 's'])
printCompMove(compMove)

if(userMove == compMove) :
    youTied()
if(userMove == 'r') :
    if(compMove == 'p') :
        youLose()
    elif(compMove == 's') :
        youWin()
elif(userMove == 'p') :
    if(compMove == 'r') :
        youWin()
    elif(compMove == 's') :
        youLose()
elif(userMove == 's') :
    if(compMove == 'r') :
        youLose()
    elif(compMove == 'p'):
        youWin()