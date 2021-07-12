#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
localWeather.py
Created on Mon Jul 12 16:27:02 2021

@author: paulmason

program that opens the browser to the URL for your local weather
what weather url looks like for Cleveland (zip = 44126):
    https://weather.com/weather/today/l/44126:4:US

steps:
    1. ask the user where they are from getting their zipcode
    2. create the url as'https://weather.com/weather/today/l/' + zipcode + ':4:US'
    3. use webbrowser's open method to open to the local weather page requested
"""

#import webbrowser for its open method
import webbrowser

#explain program
print('This program opens your browser to your local weather on weather.com.')
#prompt the user
print('Please enter your zip code to see today\'s forecast.')
#set zipcode to input given
zipcode = input()

#now create the web address with the given zipcode
address = 'https://weather.com/weather/today/l/' + zipcode + ':4:US'

#open the address using webbrowser to complete the program 
webbrowser.open(address)