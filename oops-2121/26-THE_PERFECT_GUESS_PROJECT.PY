"""We are going to write a program that generates a random number and asks the user to guess it.
if the players guess is higher than the actual number, the program displays "lower number please" . similarly, if the users guess is too low, then the program prints "higher number please". when the user guesses the correct number , the program displays the number of guesses the player made to arrive at the correct answer. """

#hint ---- USE RANDOM MODULE.

import random
n= random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses += 1
    a = int(input("guess a  number:"))
    if (a >n):
        print("lower number please")
    else:
        print("higher number please")
        
print(f"you have guessed the number correctly in {guesses} attempts")    
        