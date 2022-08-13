import random

def computerGuessMessage (randNum) :
    result = input(f"Is {randNum} too high (h), too low (l), or correct (c)?? ")
    return result

roof = 1000
print(f"Welcome! Please think of an integer between 1 and {roof}")

lastHighest = roof
lastLowest = 1
computerGuess = random.randint(lastLowest, lastHighest)
ans = computerGuessMessage(computerGuess)
while(ans != 'c') : 
    if(ans == 'h') :
        lastHighest = computerGuess
    elif(ans == 'l') :
        lastLowest = computerGuess
    computerGuess = random.randint(lastLowest, lastHighest)
    ans = computerGuessMessage(computerGuess)

print(f"The computer guessed correctly! The correct number was: {computerGuess}")