#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:23:19 2021

@author: paulmason
program to detect if a password is strong or not
a strong password is defined as at least 8 characters long, has both upper and lowercase letters
and has at least one digit
"""
#import the re module for regular expressions
import re

#create a regex pattern with at least: 1 lower, 1 upper, 1 digit and 8 characters
passRegex = re.compile(r'''(
    ^             #start anchor
    (?=.*[A-Z])   #string has 1 upper case character
    (?=.*[a-z])   #string has 1 lower case character
    (?=.*[0-9])   #string has 1 digit
    .{8,}         #ensure string is of length 8 
    $             #end anchor
)''', re.VERBOSE)

#main loop of the program
while True:
    #prompt user
    print("Input a password to see if it is strong or not:")
    print("To exit press Enter (input nothing).")
    #get input
    password = input()
    
    #break out if password is nothing
    if password == '':
        break
    
    #debug printout
    #print(mo.group())
    
    #if mo.group == None then the password is not strong
    if passRegex.search(password) == None:
        print(password + " is not a strong enough password!")
    else:
        #else it is a strong password since the search was not null
        print(password + " is a strong password!")