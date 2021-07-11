#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:23:36 2021
debugCoinToss.py
@author: paulmason
this project I was given a program for the user to guess heads or tails on a coin flip
unfortunately the code does not work as planned so will use the logging module to debug
"""

#import the logging module and set the basicConfig
import logging
logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(level)s - %(message)s')

#disable logging AFTER DONE DEBUGGING
#logging.disable(logging.CRITICAL)

#here is the code given from https://automatetheboringstuff.com/2e/chapter11/
import random

#debug output the beggining of the program
logging.debug('Start of the program.')
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    #post what the guess entered was
    logging.debug('Guess entered is: ' + guess)
    
toss = random.randint(0, 1) # 0 is tails, 1 is heads

#now actually set coinValue to toss whether it is 0 or 1
if toss == 1:
    coin = 'heads'
else:
    coin = 'tails'
    
if coin == guess:
    #post what the guess and coin value are
    logging.debug('Guess is ' + guess + ' and coin value is ' +  coin)
    print('You got it!')
else:
    #post what the guess and coin value are
    logging.debug('Guess is ' + guess + ' and coin value is ' + coin)
    print('Nope! Guess again! Correct value was: ' + coin)
    #get a new random value for a coin flip
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    
    #now actually set coinValue to H/T whether it is 1 or 0
    if toss == 1:
        coin = 'heads'
    else:
        coin = 'tails'
        
    guess = input()
    
    if coin == guess:
        #post what the guess and coin value are
        logging.debug('Guess is ' + guess + ' and coin value is ' + coin)
        print('You got it!')
    else:
        #post what the guess and coin value are
        logging.debug('Guess is ' + guess + ' and coin value is ' + coin)
        print('Nope. You are really bad at this game. Correct value was: ' + coin)
        
#output the end of the program
logging.debug('End of the program.')
        
