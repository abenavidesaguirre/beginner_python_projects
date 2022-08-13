import random

def guess(roof):
    randomNumber = random.randint(1, roof)
    userGuess = -1
    while(userGuess!=randomNumber) : 
        userGuess = int(input(f"Guess the number between 1 and {roof}: "))
        if(userGuess < randomNumber) :
            print(f"Try again. Your guess {userGuess} is LESS THAN the mystery number")
        elif(userGuess > randomNumber) : 
            print(f"Not quite. Your guess {userGuess} is GREATER THAN the mystery number")
    print(f"\nYou got it! The correct number was: {userGuess}")
guess(10)