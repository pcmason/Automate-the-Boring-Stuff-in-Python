#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openYelpPage.py
Created on Tue Jul 13 23:08:54 2021

@author: paulmason

program that goes on yelp for the business and location given by the user using Yelp
would like to make the page open down to the reviews, but I am not sure that is possible with 
the webbrowser module

yelp link looks like:
    https://www.yelp.com/biz/<shop-and-location-details>

steps:
    1. prompt the user for what business and location they want to search
    2. convert the prompt from a string to a list
    3. use webrowser to open the page on Yelp 
"""

#import the webbrowser module to open the page
import webbrowser

#step 1
#explain program
print('Enter a business and location to pull up a Yelp review for the business.')
#prompt user for business
print('Enter a business:')
biz = input()
#prompt user for location
print('Enter a location:')
loc = input()

#combine biz and loc
review = biz + ' ' + loc

#step 2
#replace all spaces in review with hypens so the webbrowser function works
review = review.replace(' ', '-')

#step 3
#use webbrowser to open the Yelp page
webbrowser.open('https://www.yelp.com/biz/' + review)