#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
twentyFortyEight.py
Created on Mon Jul 19 19:14:07 2021

@author: paulmason

program that uses selenium to open the 2048 game (found here: https://gabrielecirulli.github.io/2048/)
and continually enters Up, Right, Down and Left on the arrow keys

steps:
    1. import from selenium Keys and webdriver, use the webdriver to open to the page given above
    2. get the game container to send the keystrokes to
    3. make a while loop to continually go up, right, down and left
"""

#step 1
#import selenium and the webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import time cause selenium moves too fast sometimes
import time

#create the safari webdriver browser
browser = webdriver.Safari()
#make the window big or you cannot see the game being played
browser.maximize_window()
#open the 2048 game
browser.get('https://gabrielecirulli.github.io/2048/')

#sleep for 3 seconds while the page loads
time.sleep(1)

#step 2
#get the game element to send the keys to 
gameElem = browser.find_element_by_class_name('game-container')

#step 3
#create an infinite while loop since there is not an easy way for the bot to tell when the game is over
while True :
    try: 
        #go up
        gameElem.send_keys(Keys.UP)
        #go right
        gameElem.send_keys(Keys.RIGHT)
        #go down
        gameElem.send_keys(Keys.DOWN)
        #go left
        gameElem.send_keys(Keys.LEFT)
    except:
        #this occurs when the user stops the session after the game is over
        print("Game Over!!")
        #break from the infinite loop
        break
