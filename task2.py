"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
def title():
    print("This is a number guessing game.")

def game():
    import random
    x = 0
    n = random.randrange(1, 10)
    guess = int(input("Enter a number: "))
    if guess < n:
        print("Too low")
    elif guess > n:
        print("Too high")
    else:
        print("correct")
       
title()
game()
