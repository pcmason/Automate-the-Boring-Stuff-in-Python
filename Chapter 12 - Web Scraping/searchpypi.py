#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
searchpypi.py
run program on mac: python3 searchpypi.py <SEARCH TERM>
Created on Tue Jul 13 14:52:54 2021

@author: paulmason

program searches for a term (entered on the command line) on the Python Package Index
https://pypi.org and opens all of the top search results returned in a new browser
what search results page looks like: https://pypi.org/search/?q=<SEARCH_TERM_HERE>

steps:
    1. Read the cmd line argument from sys.argv
    2. Fetch the search results page with the requests module
    3. Find the links to each search result
    4. Call webbrowser.open() function to open the webbrowser
    
"""
#import requests to get search results page, sys for cmd line arguments argv,
#webbrowser to open the search results and bs4 to find the search result links in the HTML
import requests, sys, webbrowser, bs4

#display this message while downloading the search results page
print('Searching...')
#create the request by using the cmd line argument given
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
#check if an error occurred downloading the search page
res.raise_for_status()

#retrive top search result links
#create the BeautifulSoup object for the search results requested
soup = bs4.BeautifulSoup(res.text , 'html.parser')

#open a browser tab for each result
#all search result links on pypi have the class 'package-snippet' so pull all elements with that class
searchElems = soup.select('.package-snippet')

#either open the first 5 results or if there are less, then just open all the results that show up
numOpen = min(5, len(searchElems))

#loop through all of the links you have grabbed
for i in range(numOpen):
    #create the url to be opened
    urlToOpen = 'https://pypi.org' + searchElems[i].get('href')
    #tell the user what page is being opened
    print('Opening', urlToOpen)
    #use the webbrowser's open method to actually open the url
    webbrowser.open(urlToOpen)



