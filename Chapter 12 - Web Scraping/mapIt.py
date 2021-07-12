#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 20:42:13 2021

@author: paulmason

program that will take street address from clipboard or cmd line and open the Google Maps
page for it.
steps of the program:
    1. get street address from clipboard/cmd line
    2. open the web browser to the Google Maps page for the address

what the GoogleMaps URL will look like: https://www.google.com/maps/place/your_address_string

RUNFILE ON MAC: python3 mapIt.py {enter your address}
{} not required in terminal

"""

#import webbrowser to open the address on GoogleMaps and sys for cmd line arguments
import webbrowser, sys
#import pyperclip for the paste method to get the address from clipboard if not on cmd line
import pyperclip

#if there is more than one arg in cmd line, then address is on the cmd line
if len(sys.argv) > 1:
    #get the address from the cmd line
    #use join() since each space represents a new cmd line argument 
    address = ' '.join(sys.argv[1:])
#else the address is on the clipboard
else:
    #get address from clipboard
    address = pyperclip.paste()
    
#finally just open the page adding your address to the URL posted in the multi-line comment above
webbrowser.open('https://www.google.com/maps/place/' + address)
        

    
    