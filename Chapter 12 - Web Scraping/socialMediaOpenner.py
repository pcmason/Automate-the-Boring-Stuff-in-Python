#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
socialMediaOpenner.py
Created on Mon Jul 12 16:40:17 2021

@author: paulmason

program that automatically opens multiple social media sites in your browser
for me, I will use Instagram, Facebook, Twitter and Tumblr
to change the sites openned just edit socialSites in the program below 

what urls look like:
    https://www.facebook.com
    https://twitter.com (can add www. and it will still work)
    https://www.instagram.com
    https://www.tumblr.com

steps: 
    1. create list of all social media websites that user wants to open
    2. loop through sites creating the url to be opened as such:
        'https://www.' + site + '.com'
    3. then use webbrowsers open method to open the url given until the list has been looped over
"""

#import webbrowser for its open method
import webbrowser

#create a list of social media sites to be openned (all strings for string concat.)
socialSites = ['facebook', 'twitter', 'instagram', 'tumblr']

#loop through the sites in socialSites
for site in socialSites:
    #create the url address as described above
    address = 'https://www.' + site + '.com'
    #and then open the site in the browser
    webbrowser.open(address)
