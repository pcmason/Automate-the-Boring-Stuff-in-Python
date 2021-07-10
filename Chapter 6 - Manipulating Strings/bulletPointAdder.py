#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:28:17 2021

@author: paulmason
"""
#program will get text from the clipboard, add a star and a space to the beginning of each line, 
#then paste the new text 

#import pyperclip to use the copy() and paste() functions
import pyperclip

#paste text from the clipboard
text = pyperclip.paste()

#separate lines and add stars
#separate lines from the clipboard based on the newline character
lines = text.split('\n')

#loop through all indexes in lines
for i in range(len(lines)):
    #add the star to each string in lines
    lines[i] = '* ' + lines[i]

#combine the strings in lines into one string separated by newline characters
text = '\n'.join(lines)

#copy the new text to the clipboard
pyperclip.copy(text)