# First project
# oncepts needed: print, while loop, if/else statements, random function, input/ output

import random

def whats_the_number ():
    right_number = random.randrange(1, 10)
    guess = 0
    
    while guess != right_number:
        guess = int(input("Input your guess here: "))
        if guess > right_number:
             print("Your guess is too high")
             
        elif guess < right_number:
             print("Your guess is too low")

    return "You have guessed the right number, congrats!"

print(whats_the_number())

def whats_the_number_tries():
    