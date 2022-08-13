import random

playerToken = (input ("Welcome to Tic Tac Toe! Please select X or O: ")).upper()
computerToken = 'X'
if(playerToken == 'X') :
    computerToken = 'O'


gameBoard = [' '] * 9
turn = random.choice(['X', 'O'])
moves = 9

def checkValidSquare(square) :
    isValid = True
    if(gameBoard[square] != ' ') :
        if(turn == playerToken):
            print("Square is already taken. Please choose an empty square")
        isValid = False

    return isValid
    

def moveMessage(token, square) :
    print(f"\n\n{token} makes a move to square {square}\n")


def displayGameBoard():
    index = 0
    while(index < 9) :
        print(f"| {gameBoard[index]} |", end='')
        if(index == 2 or index == 5) :
            print('\n')
        index += 1
    print()

def makeMove () :
    while(True):
        if(turn == playerToken) :
            square = int(input(f"{playerToken}'s turn. Input move (0-8): "))
        else :
            square = random.randint(0,8)
        isValid = checkValidSquare(square)
        if(isValid) :
            break
    moveMessage(turn, square)
    gameBoard[square] = turn
    displayGameBoard()
    global moves
    moves -= 1

def switchPlayer() :
    global turn
    if (turn == playerToken) :
        turn = computerToken
    else :
        turn = playerToken

def checkForRow() :
    check = 0
    index = 0
    while(check < 3) :
        if(gameBoard[index] == gameBoard[index + 1] == gameBoard[index + 2]) :
            return gameBoard[index]
        index += 3
        check += 1
    
def checkForCol() :
    check = 0
    index = 0
    while(check < 3) :
        if(gameBoard[index] == gameBoard[index + 3] == gameBoard[index + 6]) :
            return gameBoard[index]
        index += 1
        check+=1

def checkForDiagonal() :
    if(gameBoard[0] == gameBoard[4] == gameBoard[8]) :
        return gameBoard[0]
    if(gameBoard[2] == gameBoard[4]== gameBoard[6]) :
        return gameBoard[2]

def checkForWinner() :
    rowWinner = checkForRow()
    if(rowWinner) :
        print("DEBUG - row")
        return rowWinner
    colWinner = checkForCol()
    if(colWinner) :
        print("DEBUG - col")
        return colWinner
    diagonalWinner = checkForDiagonal()
    if(diagonalWinner) :
        print("DEBUG - diag")
        return diagonalWinner
    

while(moves > 0) :
    makeMove()
    if(moves <= 4): 
        winner = checkForWinner()
        if(winner and winner != ' ') :
            print(f"\n{winner} is the Winner!")
            exit()
    switchPlayer()
    print(f"DEBUG = moves; {moves}")
print("It's a tie!")
