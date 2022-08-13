import random
from words import words

secretWord = (random.choice(words)).upper()
numLives = 5
wordStatus = ['_'] * len(secretWord)
lettersGuessed = []

def welcomeMessage() :
    print(f"\nWelcome to hangman! \n The word you are trying to guess has {len(secretWord)} letters. You have {numLives} lives. Good Luck! \n")

def gameStatus() :
    print(f"Lives Left: {numLives}")
    print(f"Current Word: ", end= '')
    print (*wordStatus)
    print(f"Letters guessed: ", end ='')
    print(*lettersGuessed)

def playerGuess():
    while(True) :
        letterGuess = (input("Please guess a letter: ")).upper()
        isInvalidGuess = False
        for letter in lettersGuessed :
            if letter == letterGuess :
                print("DEBUG: letter already guessed")
                isInvalidGuess = True
                break
        if(not isInvalidGuess) : 
            break

    lettersGuessed.append(letterGuess)
    index = 0
    isCorrectGuess = False
    for letter in secretWord :
        if letter == letterGuess :
            wordStatus[index] = letterGuess.upper()
            isCorrectGuess = True
        index += 1
        
    if (isCorrectGuess) :
        print(f"\nWell done! {letterGuess.upper()} is a correct letter \n")
    else :
        global numLives
        numLives -= 1
        print(f"\nUh oh! That guess was incorrect. You have {numLives} remaining \n")



welcomeMessage()

while(numLives >=1 and wordStatus != secretWord) :
    gameStatus()
    playerGuess()

if(numLives < 1) :
    print(f"Game Over! The correct word was: {secretWord}")
elif(wordStatus == secretWord) :
    print(f"You Win! The correct word was: {secretWord} ")