#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 00:34:12 2021

@author: paulmason
"""
#code that creates a back-and-forth zigzag animation

#import modules: sys for exit() and time for sleep() 
import sys, time

#set how many spaces to indent 
indent = 0
#set whether the indent is increasing or not
indentIncreasing = True

try:
    #the main program loop
    while True:
        #print the correct number of indentations
        print(" " * indent, end = "")
        #print the pattern
        print("*******")
        #pause for a tenth of a second so it is not moving too fast
        time.sleep(0.1)
        
        #create an 'animation' by changing the indent from left to right
        #animation will only stop when user terminates program, this is an infinite loop
        #left-right animation
        if indentIncreasing:
            #increase the number of spaces
            indent = indent + 1
            #change direction at indent = 20 (could be any number - impacts length of side-side animation)
            if indent == 20:
                #once you hit the number go to the else statement
                indentIncreasing = False
                
        #right-left animation        
        else:
            #decrease the number of spaces
            indent = indent - 1
            #change direction at indent = 0
            if indent == 0:
                #go to the true part of the if-statement to animate to the right
                indentIncreasing = True
                
#call KeyboardInterrupt to allow the user to stop the running of the program with ctrl+c
except KeyboardInterrupt:
    #terminate the program
    sys.exit()
    

        