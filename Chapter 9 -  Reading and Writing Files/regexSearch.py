#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 02:29:24 2021

@author: paulmason
program opens all .txt files in a folder searching for a specific REGEX pattern
here the pattern is 'Paul is Cool', which I placed in a file in the madlib file I created
for the last project madlib.py
"""

#import the regex library
import re
#import pathlib to use path
from pathlib import Path

#create regex patten to search for
findre = re.compile(r'Paul is cool.')

#get the path to the madlib file
madlibPath = Path('/Users/paulmason/Desktop/Automate_Boring_Stuff/madlib')

#loop through all the txt files in the madlib folder using glob
for filename in madlibPath.glob('*.txt'):
    #open the file
    filename = open(filename)
    #use readlines to get each line of the file
    text = filename.readlines()
    #keep track of what line this is
    lineNumber = 0
    
    #loop through each line in text
    for line in text:
        #append lineNumber 
        lineNumber += 1
        #check if lines matches the pattern
        mo = findre.search(line)
        if mo != None:
            #print out the file the message was found in and what line
            print("Pattern found in: " + str(filename) + " at line " + str(lineNumber))
