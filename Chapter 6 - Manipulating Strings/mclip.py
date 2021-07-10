#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 16:55:11 2021

@author: paulmason
"""
#a multi-clipboard that is used to easily copy and paste common email responses

#create a dict that has a key as a generic type of response and the value as the email response
TEXT = {'agree': """Yes, I agree that sounds fine to me.""",
        'busy': """Sorry, can we do this either later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

#import sys to use the sys.argv variable, import pyperclip to use its copy() and paste() functions
import sys, pyperclip

#check if sys.argv has fewer than 2 values in it
if len(sys.argv) < 2:
    #display a message to the user that they forgot to add the key 
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    #terminate the program
    sys.exit()
    
#the second element in sys.argv is the command line arg
keyphrase = sys.argv[1]

#check if keyphrase entered is one of the keys in TEXT
if keyphrase in TEXT:
    #copy the value in TEXT associated with keyphrase
    pyperclip.copy(TEXT[keyphrase])
    #tell the user the value has been copied to the clipboard
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    #then keyphrase is not in TEXT so there is no associated value for it
    print('There is no text for ' + keyphrase)

