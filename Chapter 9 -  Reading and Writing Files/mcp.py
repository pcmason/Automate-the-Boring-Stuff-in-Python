#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:01:17 2021

@author: paulmason
"""
#program to save and load pieces of text to the clipboard
#Usage: py.exe mcb.pyw save <keyword> -Saves clipboard to keyword
#       py.exe mcb.pyw <keyword>      -Loads keyword to the clipboard
#       py.exe mcb.pyw list           -Loads all keywords to clipboard

#import pyperclip for copying and pasting
import pyperclip
#import sys to read command line arguments
import sys
#import shelve to save clipboard text to a file and loads the text from the shelve file
import shelve

#the shelve file will be prefixed with mcb
mcbShelf = shelve.open('mcb')

#save clipboard content
#know they have called save if there are 2 command-line arguments and the second one is save
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    #the keyword will be the key for mcbShelf and the value will be the text currently on the clipboard
    mcbShelf[sys.argv[2]] = pyperclip.paste()
#if only 1 cmd line argument then either list or the load keyword was called
elif len(sys.argv) == 2:
    #list keywords and load content
    #check if argument was list
    if sys.argv[1].lower() == 'list':
        #copy a list of strings of the keywords to the keyboard
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        #assume that the associated value for the key should be loaded onto the cb (if key exists)
        pyperclip.copy(mcbShelf[sys.argv[1]])

#close the shelve file
mcbShelf.close()