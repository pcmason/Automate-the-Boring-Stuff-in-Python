#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 02:07:15 2021

@author: paulmason
"""
#this program creates Collatz function and has the user run it
#collats function divides number given by 2 if the number is even
#if the number is odd then it multiplies the number by 3 and adds 1 to that

#this function will run the collatz function until it returns 1
def collatz(number):
    #create the main loop that is broken when number = 1
    while number != 1:
        #print out the number
        print(number)
        #check if number is even or odd and not equal to 1
        if number % 2 == 0:
            #if even divide number by 2
            number = number // 2
        elif number % 2 == 1 and number != 1:
            #if odd (and not 1) multiply the number by 3 and add 1
            number = number * 3 + 1
    #print the last one
    print(number)
        
#tell the user what to do
print("Enter a number:")

#get the input for the number also use a try to ensure the user enter a number
try: 
    userNumber =int(input())
    #call the collatz function
    collatz(userNumber)
except ValueError: 
    #this error message will appear if the user does not enter an integer
    print("User must enter a whole number!")



    