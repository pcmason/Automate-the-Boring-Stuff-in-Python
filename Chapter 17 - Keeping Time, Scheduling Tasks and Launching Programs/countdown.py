#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
countdown.py
Created on Thu Aug 19 12:56:53 2021

@author: paulmason

a simple countdown program that plays an alarm when the countdown is over (will be a minute countdown)

steps:
    1. Count down from 60 seconds
    2. Play a sound file (alarm.wav) when the countdown has reached 0
"""

#import time to use sleep to countdown from 60 and subprocess to use Popen to open the alarm file
import time, subprocess

#step 1 - count down
#set time to be 60 seconds
timeLeft = 60
#loop until time is  0
while timeLeft > 0:
    #display time
    print(timeLeft, end = ' ')
    #wait a second
    time.sleep(1)
    #lower the value for timeLeft
    timeLeft -= 1
    
#step 2 - play a sound file at the end of the countdown
#use the Popen to open the file alarm.wav in the cd
subprocess.Popen(['open', 'alarm.wav'])
