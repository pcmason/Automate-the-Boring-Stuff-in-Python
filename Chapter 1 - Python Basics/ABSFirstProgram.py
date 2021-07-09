#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 00:24:58 2021

@author: paulmason
"""
#First program in Automate the Boring Stuff
#This program will ask for a person's name and number

#the print() function prints the value in the '' on the screen
print('Hello World!')
print('What is your name?') #ask the user for their name

#input() function waits for the user to type something then hit enter
myName = input()

#using string concatenation in the print function
print('It is good to meet you ' + myName)

print('The length of your name is:')
#use len() to get the number of characters in a string
print(len(myName))

print('What is your age?') #ask the user for their age
myAge = input()

#use int() to convert the user's input for age to a number
#then use str() to integer age added by one back into a string for print()
print('You will be ' + str(int(myAge)+1) + ' in one year.')