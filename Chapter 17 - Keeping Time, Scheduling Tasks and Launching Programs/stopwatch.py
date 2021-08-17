#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stopwatch.py
Created on Mon Aug 16 19:17:52 2021

@author: paulmason

program that emulates a real-life stopwatch

steps:
    1. track the amount of time elapsed between presses of the Enter key, with each press starting
       a new 'lap' on the timer
    2. print the lap number, total time, and lap time
"""
#import time to use its time() method to get the current time for the stopwatch
import time

#step 1 - setup the program to track times
#display program instructions to user
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
#use input to have the user press ENTER to begin
input()
print('Started.')
#get the first-lap's start-time
startTime = time.time()
lastTime = startTime
#set the lap count to 1 for the beginning of the program
lapNum = 1

#step 2 - track and print lap times
#start tracking the lap times, use the try statement to handle the CTRL-C used to end the program
try:
    #infinite loop until user hits CTRL-C (to match a stopwatch)
    while True:
        #once user presses ENTER that ends a lap
        input()
        #use round to make the times much easier to read for the user, rounding to 2 decimal points
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        #add the end parameter to avoid double-spacing the output
        print('Lap %s: %s (%s)' % (lapNum, totalTime, lapTime), end = '')
        lapNum += 1
        #reset the lap time
        lastTime = time.time()
except KeyboardInterrupt:
    #handle the CTRL-C exception to prevent the error message from being printed out
    print('\nDone.')