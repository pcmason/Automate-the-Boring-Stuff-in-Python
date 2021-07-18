#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cmdLineEmail.py
run program on mac: python3 cmdLineEmail.py <EMAIL> <MESSAGE_CONTENTS_HERE>
Created on Sat Jul 17 17:20:30 2021

@author: paulmason

program that takes an email address and a string of text on the command line 
and uses selenium to log into your email account and sends an email of the 
string to the provided address given

This will most likely only work on Gmail as many of the CSS selectors are quite specific

steps: 
    1. prompt the user for their password, enter your email at the top of the program
    2. click on the 'Compose an email' button (CSS selector = 'div.T-I.T-I-KE.L3')
    3. fill in the to <textarea> box (name = 'to')
    4. enter a basic subject line "Automated Message" (name = 'subjectbox')
    5. fill in the message box area (CSS selector = 'div.Am.Al.editable.LW-avf.tS-tW')
    6. send the email 
"""

#import selenium to control the browser and sys to read in the cmd line arguments
#and pyinputplus to get the email account password from the user
from selenium import webdriver
import sys, pyinputplus
#also import the Keys module to use the ENTER button for login
from selenium.webdriver.common.keys import Keys
#import the timer function to make the program wait so it does not go too fast
import time

#set the email address the message will be sent from as a constant
#change this is your name is not Paul Channing Mason
######UNCOMMENT THIS LINE AND PLACE YOUR EMAIL HERE WHEN YOU RUN THE PROGRAM##############################
#EMAIL_SENDER = "paulmasonchan33@gmail.com"

#step 1
#prompt user for their email password
print('Please enter your password for the email account: %s' % EMAIL_SENDER)
#use pyinputplus's inputPassword() method to get the password
password = pyinputplus.inputPassword()

#ensure the program was given more than one cmd line arguments
if len(sys.argv) < 2:
    #alert the user they did not enter a recipient to the program
    print('No email address specified as a recipient!')
    #exit the program
    sys.exit()
#check if a message was give (can only be one word like 'hello' that is fine)
elif len(sys.argv) < 3:
    #alert the user that a message was not specified in the program
    print('No message given to send!')
    #exit the program
    sys.exit()
#everything has went well
else:
    #set the email recipient as the second cmd line argument
    sendEmailTo = sys.argv[1]
    #set the message to the rest of the cmd line arguments
    message = ' '.join(sys.argv[2:])
    
#open Safari with the webdriver
browser = webdriver.Safari()
#use the webdriver to go to gmail
browser.get('https://mail.google.com/')

#get the elem for the email input (id = 'identifierId')
inputEmailElem = browser.find_element_by_id('identifierId')
#input the constant email address set above
inputEmailElem.send_keys(EMAIL_SENDER)
#attempt to use Keys.ENTER to enter the username
inputEmailElem.send_keys(Keys.ENTER)
#cannot just hit submit() on inputEmailElem so must get the element for the Next button
#the class name is 'VfPpkd-RLmnJb'
#nextButtonElem = browser.find_element_by_class('VfPpkd-RLmnJb')

#wait 5 seconds
time.sleep(5)

#get the elem for the password input next (name = 'password')
passwordElem = browser.find_element_by_name('password')
#enter the password entered into the password element
passwordElem.send_keys(password)
#submit the password element 
passwordElem.send_keys(Keys.ENTER)

#wait 5 seconds again
time.sleep(5)

#step 2
#get the element for the compose email button
composeEmailElem = browser.find_element_by_css_selector('div.T-I.T-I-KE.L3')
#click on the compose email button
composeEmailElem.click()

#wait 2 seconds
time.sleep(2)

#step 3
#get the element to fill in the 'To' box in the email box
toElem = browser.find_element_by_name('to')
#fill in the box with the second argument in the cmd line, the recipient of the automated msg
toElem.send_keys(sendEmailTo)

#step 4
#get the element for the Subject line
subjectLineElem = browser.find_element_by_name('subjectbox')
#fill in the box with a generic message like "Automated Message" or whatever you want
subjectLineElem.send_keys('Automated Message from Paul Mason')

#step 5
#get the element for the message box 
messageBoxElem = browser.find_element_by_css_selector('div.Am.Al.editable.LW-avf.tS-tW')
#fill in the message with the message given in the cmd line
messageBoxElem.send_keys(message)

#wait 1 second
time.sleep(1)

#step 6
#find the send button with its specific CSS selector (quite long)
nextButtonElem = browser.find_element_by_css_selector('div.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
#finally click the next button
nextButtonElem.click()


#output the the user that the program worked
print('Success! Emailed \'' + message + '\' to: ' + sendEmailTo)



