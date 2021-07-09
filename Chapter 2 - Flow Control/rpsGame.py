#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 21:02:15 2021

@author: paulmason
"""
#this is a rock paper scissors game

#import the modules: sys for  exit() and random for randint()
import random, sys

#print the name of the game
print("ROCK, PAPER, SCISSORS")

#create vars to keep track of wins, losses and ties
wins = 0
losses = 0
ties = 0

while True: #the main game loop
    #print the number of wins losses and ties
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    #the player input loop
    while True: 
        #prompt the player to make a move 
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        #get the players move
        playerMove = input()
        #if the player quits the game
        if playerMove == 'q':
            #exit the program
            sys.exit()
        #if the player makes a move
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            #break out of the player input loop
            break
        #remind player to enter one of r, p, s or q
        print("Type one of r, p, s or q.")
        
    #display what the player chose
    if playerMove == 'r':
        #if the player chose rock
        print('ROCK versus...')
    elif playerMove == 'p':
        #if the player chose paper
        print('PAPER versus...')
    elif playerMove == 's':
        #if the player chose scissors
        print('SCISSORS versus...')
    
    #display what the computer chose
    #the computer chooses by picking a random int between 1 and 3
    randNum = random.randint(1, 3)
    #assign r, p and s for 1, 2 and 3 respectively
    if randNum == 1:
        computerMove = 'r'
        print('ROCK')
    elif randNum == 2:
        computerMove = 'p'
        print("PAPER")
    elif randNum == 3:
        computerMove = 's'
        print("SCISSORS")
    
    #update the records for win/loss/tie
    #scenario of a tie
    if playerMove == computerMove:
        print("It is a tie!")
        ties = ties + 1
    #player chooses rock and comp chooses scissors (W)
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    #player chooses paper and comp chooses rock (W)
    elif playerMove == 'p' and computerMove == 'r':
        print("You win!")
        wins = wins + 1
    #player chooses scissors and comp chooses paper (W)
    elif playerMove == 's' and computerMove == 'p':  
        print("You win!")
        wins = wins + 1
    #player chooses rock and comp chooses paper (L)
    elif playerMove == 'r' and computerMove == 'p':
        print("You lose!")
        losses = losses + 1
    #player chooses paper and comp chooses scissors (L)
    elif playerMove == 'p' and computerMove == 's':
        print("You lose!")
        losses = losses + 1
    #player chooses scissors and comp chooses rock (L)
    elif playerMove == 's' and computerMove == 'r':   
        print("You lose!")
        losses = losses + 1
    