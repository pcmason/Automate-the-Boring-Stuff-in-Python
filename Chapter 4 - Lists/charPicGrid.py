#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 01:58:47 2021

@author: paulmason
"""
#print out a grid of characters with a function called charPrinter

#create the that prints out every element in a 2D list
def charPrinter(givenChar):
    #loop through the column
    for y in range(len(givenChar[0])):
        #loop through each element in each column
        for x in range(len(givenChar)):
            #print out the character at the given location
            print(givenChar[x][y], end = '')
        #print a newline so that all of the characters look like a 2D array
        print()
        
#example grid to use
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#call the charPrinter function sith the example grid
charPrinter(grid)