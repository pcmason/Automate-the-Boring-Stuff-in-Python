#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 02:03:59 2021

@author: paulmason
program that is designed to keep an idiot busy for a long amount of time
"""


#import the pyinputplus module to take only yes/no input with inputYesNo() function
import pyinputplus as pyip

#create the main loop for the program
while True:
    #prompt the user
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    #get the response from the user
    response = pyip.inputYesNo(prompt)
    
    #exit the program if the user enters no, else continue looping to keep the user busy
    if response == "no":
        break
    

#end the program
print("Thank you, have a nice day.")