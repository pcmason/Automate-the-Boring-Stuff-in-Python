#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openAllLinks.py
Created on Mon Jul 12 16:21:14 2021

@author: paulmason

program that will open all links on a page in separate browser tabs
this will need bs4, which I have not went over yet so cannot complete

there will be two ways this program can be run:
    1. using the constant link for Sweigart's Automate the Boring Stuff's About page: https://inventwithpython.com/about.html
    2. letting the user input their own webpage
    
cannot do both at the same time, recommend running both
also make use of webbrowser.open_new_tab(url) method

steps:
    1. Set the address using step 1 or 2 above
    2. Use requests module to download the address set in step 1
    3. Use bs4 to select() all elements of 'a' 
    4. Use webbrowser to open() all of the links you have selected
"""

#import webbrowswer for the open() method and bs4 to select all HTML <a> elements
#and requests to download the address specified
import webbrowser, bs4, requests

####IMPORTANT###
#method 1 or method 2 must be commented out, cannot have both running or 
#method 2 will override method 1

#step 1
#method 1
#set the address to the link specified above for ABSWP
#address = 'https://inventwithpython.com/about.html'

#method 2
#prompt user for web address
print('Please enter the url of a website you want to open all links to in new tabs:')
#set the address to input given by the user
address = input()

#step 2
#use requests to download the address specified
res = requests.get(address)
#make sure res does not return an Exception
res.raise_for_status()

#step 3
#create the BeautifulSoup object from res
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#now select all <a> elements on the page given
pageLinks = soup.select('a')

#step 4
#open all links on the page (this will be a lot of links)
for link in pageLinks:
    #print(link.get('href'))
    #only open links that start with 'https'
    if  (link.get('href') != None) and (link.get('href').startswith('https')):
        #use webbrowser to open each link using get to specify the href attribute
        webbrowser.open(link.get('href'))


