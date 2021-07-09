#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 01:18:33 2021

@author: paulmason
"""
#this is a program to see how often a streak of 6 heads/tails occurs in a list of 100 coin flips

#import the random module for randing() to decide if coin is H or T
import random
#keep a counter for the number of streaks
numStreaks = 0
#run the experiment 10,000 times
for experimentNum in range(10000):
    #code that creates 100 head/tail values
    #create an array to hold the values
    coins = []
    #create var to hold old number of streaks (to ensure it does not count all streaks of 6 in the next loop)
    oldStreaks = numStreaks + 1
    #loop through 100 times to add head/tail
    for i in range(100):
        #use randint to decide if the value is a head or a tail
        if random.randint(0,1) == 1:
            #add a head for a one
            coins.append('H')
        else:
            #add a tail for a zero
            coins.append('T')  
            
    #code that checks if there is a streak of 6 heads or tails in a row
    #loop through coins
    for i in range(len(coins)-1):
        #if oldStreaks = numStreaks then break, so you do not keep counting streaks of 6
        if oldStreaks == numStreaks:
            break
        j = i+1
        #create a counter for number of heads/tails in a row
        streak = 0
        #loop through the next 5 coins after the first one
        for j in range(j+5):
            if coins[i] == coins[j]:
                #if the coins are the same add to the streak
                streak += 1
                if streak == 5:
                    #if streak equals five this is a streak of 6 in a row
                    numStreaks += 1
                    #break out of the for loop
            else:
                #else if the coins are not equal this breaks the streak so break the loop
                break

#print the results of the experiment
#which is the percentage chance of a streak of 6 in 100 coinflips
print('Chance of streak: %s%%' % (numStreaks / 100))