#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
formFiller.py
Created on Wed Sep  1 07:16:28 2021
@author: paulmason

program that takes a dictionary of data and uses pyautogui to automatically fill in the form
form link: https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform

steps:
    1. set up coordinates
    2. start typing data
    3. handle select lists and radio buttons
    4. submit the form and wait
"""

#import the pyautogui module to automate filling in the forms and the time module
import pyautogui, time

#step 1 - set up coordinates
#a hardcoded dict of the form data to be entered autonomously
formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'}
            ,{'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'}
            ,{'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'}
            ,{'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}]

#the coordinates for the submit another link button
###THIS WILL MOST LIKELY BE DIFFERENT FOR YOUR COMPUTER I FIGURED MINE OUT THROUGH A GUESS AND CHECK
submitAnotherLink = (580, 250)

#set the PAUSE variable to wait half a second after each function call
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

#step 2 - start typing data
for person in formData:
    #give the user a chance to kill the script
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    #wait until the form page has loaded
    time.sleep(5)
    
    #tell the user what person's info is being entered
    print('Entering %s info...' % person)
    #press tab twice to put the name field into focus
    pyautogui.write(['\t', '\t'])

    #fill out the Name field
    pyautogui.write(person['name'] + '\t')

    #fill out the Greatest Fear(s) field
    pyautogui.write(person['fear'] + '\t')
    
    #step 4 - handle select lists and radio buttons
    #fill out the Source of Wizard Powers field
    if person['source'] == 'wand':
        #press down arrow once for wand
        pyautogui.write(['down','enter', '\t'], 0.5)
    elif person['source'] == 'amulet':
        #press down arrow twice
        pyautogui.write(['down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'crystal ball':
        #press down arrow 3 times
        pyautogui.write(['down', 'down', 'down', 'enter', '\t'], 0.5)
    elif person['source'] == 'money':
        #press down arrow 4 times
        pyautogui.write(['down', 'down', 'down', 'down', 'enter', '\t'], 0.5)
        
    #fill out the RoboCop field
    if person['robocop'] == 1:
        #press space and move onto next question
        pyautogui.write([' ', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        #press right arrow then tab
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        #press right arrow 2 times then tab
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        #press right arrow 3 times then tab
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        #press right arrow 4 times then tab
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    #step 5 - submit the form and wait
    #fill out the Additional Comments field
    pyautogui.write(person['comments'] + '\t')

    #click submit
    #wait for the button to activate
    time.sleep(0.5)
    #hit the enter key
    pyautogui.press('enter')

    #wait until form page has loaded
    print('Submitted form.')
    time.sleep(5)

    #click the submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])



