#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 21:38:21 2021

@author: paulmason
"""
#Conway's Game of Life
#A filled square (#) is alive and an empty square is dead
#A living square with 2-3 living neighbors will continue to live
#A dead square with 3 living neighbors will come alive on the next step
#All other squares die or remain dead for the next step

#import the modules needed: random to initialize the game with randint()
#                           time to use sleep() for a pause in the animation
#                           copy for deepcopy() to get a copy of the game before things change
#                           sys for exit() to be able to use ctrl+c to exit the program
import random, time, copy, sys

#set constants for WIDTH AND HEIGHT
WIDTH = 60
HEIGHT = 20

#initialize an empty list for the game cells
cells = []
#loop through the 2D matrix and create the first state for Conway's Game of Life
for i in range(WIDTH):
    #create a new column 
    column = []
    for j in range (HEIGHT):
        #randomly decide to make the square 'alive' represented by a '#'
        if random.randint(0,1) == 0:
            #add a living cell
            column.append('#')
        else:
            #add a dead cell
            column.append(' ')
    #cells is a list of columns 
    cells.append(column)

#main program loop
try:
    while True:
        #separate each step with newlines
        print('\n\n\n\n\n')
        #copy the list of cells, since you are copying a list of lists use deepcopy()
        currentCells = copy.deepcopy(cells)
        
        #print currentCells onto the screen
        for i in range(WIDTH):
            for j in range(HEIGHT):
                print(currentCells[i][j], end = '')
            #print a newline at the end of each row
            print()
            
        #calculate the next step's cells based on currentCells
        for j in range(WIDTH):
            for i in range(HEIGHT):
                #get neighboring coordinates
                #'% WIDTH' ensure leftCoord is always between 0 and WIDTH - 1
                #this is a mod wraparound value where the left neighbor to a left most cell is the right most cell
                leftCoord = (j-1) % WIDTH
                rightCoord = (j+1) % WIDTH
                upCoord = (i-1) % HEIGHT
                lowCoord = (i+1) % HEIGHT
                
                #keep track of the number of living neighbors
                numNeighbors = 0
                if currentCells[leftCoord][upCoord] == '#':
                    #the top left neighbor is alive
                    numNeighbors += 1
                if currentCells[j][upCoord] == '#':
                    #the top neighbor is alive
                    numNeighbors += 1
                if currentCells[rightCoord][upCoord] == '#':
                    #the top right neighbor is alive
                    numNeighbors += 1
                if currentCells[leftCoord][i] == '#':
                    #the left neighbor is alive
                    numNeighbors += 1
                if currentCells[rightCoord][i] == '#':
                    #right neighbor is alive
                    numNeighbors += 1
                if currentCells[leftCoord][lowCoord] == '#':
                    #bottom left neighbor is alive
                    numNeighbors += 1
                if currentCells[j][lowCoord] == '#':
                    #bottom neighbor is alive
                    numNeighbors += 1
                if currentCells[rightCoord][lowCoord] == '#':
                    #bottom left neighbor is alive
                    numNeighbors += 1
                
                #set the cells based on the rules of Conway's Game of Life
                #RULES: living cells with 2 or 3 living neighbors live, dead cells w 3 neighbors become alive
                #every other cell dies
                
                if currentCells[j][i] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                    #living cells with 2 or 3 neighbors live
                    cells[j][i] = '#'
                elif currentCells[j][i] == ' ' and numNeighbors == 3:
                    #dead cells surrounded by 3 living cells become alive
                    cells[j][i] = '#'
                else:
                    #all other cells die
                    cells[j][i] = ' '
        #add a one-second pause to reduce flickering
        time.sleep(1)
        
#call KeyboardInterrupt to allow the user to stop the running of the program with ctrl+c
except KeyboardInterrupt:
    #terminate the program
    sys.exit()