#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:50:56 2021

@author: paulmason
program that reads in a text file and lets the user overwrite the file where 
ADJECTIVE, NOUN, VERB, ADVERB is in a sentence
"""

#import re for regex matching 
import re
#import pyinputplust to handle input errors
import pyinputplus as pyip
#import Pathlib to use Path to read to text from madlib.txt
from pathlib import Path

#open the file with the madlib
#file must be opened in read mode
mlFile = Path('/Users/paulmason/Desktop/Automate_Boring_Stuff/madlib/madlib.txt')
#write the madlib to the file so it can be run multiple times
mlFile.write_text("The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.")
#get the madlib from the file
madlib = mlFile.read_text()


#create regex pattern to determine ADJ, NOUN, VERB, ADVERB
mlRegex = re.compile(r'(ADJECTIVE|VERB|NOUN|ADVERB)+')
#find all matches for the pattern in madlib
mo = mlRegex.findall(madlib)

#loop through mo until it does not hold a value to create the madlib
for word in mo:
    #check the value of mo.group
    if word == 'ADJECTIVE':
        #adjective
        prompt = 'Enter an adjective:\n'
        adj = pyip.inputStr(prompt)
        madlib = madlib.replace('ADJECTIVE', adj, 1)
        
    elif word == 'NOUN':
        #noun
        prompt = 'Enter a noun:\n'
        noun = pyip.inputStr(prompt)
        madlib = madlib.replace('NOUN', noun, 1)
        
    elif word == 'VERB':
        #verb
        prompt = 'Enter a verb:\n'
        verb = pyip.inputStr(prompt)
        madlib = madlib.replace('VERB', verb, 1)
        
    elif word == 'ADVERB':
        #adverb
        prompt = 'Enter an adverb:\n'
        adverb = pyip.inputStr(prompt)
        madlib = madlib.replace('ADVERB', adverb, 1)

#print output to the screen
print(madlib)   
     
#now reopen the madlib.txt file and write the madlib to it
newMLFile = open('/Users/paulmason/Desktop/Automate_Boring_Stuff/madlib/madlib.txt', 'w')
newMLFile.write(madlib)
newMLFile.close()
        
    
        