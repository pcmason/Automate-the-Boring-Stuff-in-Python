#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 20:49:09 2021

@author: paulmason
"""
#This is the guess the number game

#import random module to generate a random integer to guess using randint()
import random

#create a random integer between 1 and 20
secretNumber = random.randint(1, 20)
#print out dialog to explain the prompt to the user
print("I am thinking of a number between 1 and 20.")

#ask the user to guess 6 times
for guessTaken in range(1, 7):
    #print out the prompt
    print("Take a guess.")
    #get the guess from the user and convert it to an int
    guess = int(input())
    
    #tell the user if their guess is too low or too high
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        #this is the correct answer so break
        break

#check if your guess was correct after the break or 6 attempts
if guess == secretNumber:
    #if you got the correct answer print out a congrats with the number of guesses
    print("Good job! You guessed the number in " + str(guessTaken) + " guesses.")
else:
    #tell the user the answer after 6 incorrect guesses
    print("No. The number was " + str(secretNumber))
    
    