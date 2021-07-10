#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 03:14:53 2021

@author: paulmason
"""
'''
finds phone numbers and email addresses from text on the clipboard
good example to copy to clipboard: https://nostarch.com/contactus/
'''

#import pyperclip to access and clipboard and re for regular expression matching
import pyperclip, re

#create the regex for finding phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?             #area code
    (\s|-|\.)?                     #separator    
    (\d{3})                        #first 3 digits
    (\s|-|\.)                      #separator
    (\d{4})                        #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
)''', re.VERBOSE)

#create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   #username
    @                   #symbol
    [a-zA-Z0-9.-]+      #domain name
    (\.[a-zA-Z]{2,4})   #dot-something
)''', re.VERBOSE)

#find matches in clipboard text
text = str(pyperclip.paste())

#store all phone numbers and emails into matches
matches = []

#loop through all found phone numbers
for groups in phoneRegex.findall(text):
    #set phone number to be the area code, 3 digits then last 4 digits
    phoneNumber = '-'.join([groups[1], groups[3], groups[5]])
    
    if groups[8] != '':
        #add the extension if there is one
        phoneNumber += ' x' + groups[8]
        
    #add phoneNumber to matches
    matches.append(phoneNumber)
    
#loop through all the found emails
for groups in emailRegex.findall(text):
    #just add the email to matches
    matches.append(groups[0])
    
#copy results to clipboard
#check if there are any results
if len(matches) > 0:
    #copy the matches to the clipboard
    pyperclip.copy('\n'.join(matches))
    #print out what has been copied to the clipboard
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    #print a matches if nothing is found
    print("No phone numbers or email addresses were found.")

'''what output should look like:
    Copied to clipboard:
    800-420-7240
    415-863-9900
    415-863-9950
    info@nostarch.com
    media@nostarch.com
    academic@nostarch.com
    info@nostarch.com
'''
