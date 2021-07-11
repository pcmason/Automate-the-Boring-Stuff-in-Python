#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 02:17:17 2021

@author: paulmason
program that asks the user 10 multiplication questions
"""

#import the necessary modules
#pyip to take the input from the user and check if it is within the time and try limits set
import pyinputplus as pyip
#import time for sleep() to give user a second to read Q and use random to generate the Qs
import time, random

#number of questions the program asks
numQuestions = 10
#keep track of number of correct answers
correctAnswers = 0

#loop through number of questions to ask that many questions
for qNumber in range(1, numQuestions + 1):
    #pick two random single digit numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    #create the prompt based on the two randomly generated numbers
    prompt = '#%s: %s X %s = ' % (qNumber, num1, num2)
    
    #ask the user the question
    try:
        #right answers covered by allowRegexes
        #wrong answers covered by blockRegexes with custom message
        #user has 8 seconds and 3 tries to answer question
        pyip.inputStr(prompt, allowRegexes = ['^%s$' % (num1 * num2)],
                      blockRegexes = ['.*', 'Incorrect!'],
                      limit = 3, timeout = 8)
        
    #create exception for a time limit error
    except pyip.TimeoutException:
        print('Out of time!')
    #create exception for number of attempts error
    except pyip.RetryLimitException:
        print('Out of tries!')
    
    else:
        #if no exceptions were raised then the correct answer was given
        print('Correct!')
        #append to correctAnswers
        correctAnswers += 1
        
    #give the user a one second break to read the output 
    time.sleep(1)

#print out the users score
print('Score: %s / %s' % (correctAnswers, numQuestions))