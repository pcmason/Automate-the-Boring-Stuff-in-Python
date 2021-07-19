#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
imgurDownloader.py
Created on Mon Jul 19 17:35:35 2021

@author: paulmason

program that goes to Imgur's website (https://imgur.com) and searches for category of photos and 
downloads all the resulting images.

can run this program multiple times and all images downloaded will go to the file 'imgur_downloads'

steps:
    1. prompt the user for what category of photos they want to download
    2. use the requests module to download the search results 
        url = 'https://imgur.com/search?q=' + <SEARCH+TERM>
    3. use bs4 to parse the html to find the photos (should just be all the <img> elements)
    4. use the iter_content method to download the image
"""

#import requests to download the search page and bs4 to parse for the images
#and import os to make a directory for the downloads
import requests, bs4, os

#explain the program
print('This program goes to Imgur and downloads all the images for a category of photos.')
#create the directory to download the images to 
os.makedirs('imgur_downloads', exist_ok = True)

#step 1
#prompt user to enter a category of photos to search for
print('Enter a category of photos to search for: ')
#set photos to the input given
photos = input()

#step 2
#strip all whitespaces from beginning and end of input
photos.strip()
#if mutliple words were entered for photos, replace all spaces ' ' with '+'
photos.replace(' ', '+')
#output what is being downloaded
print('Downloading page %s...' % photos)
#now use the get method to look up the photos given 
res = requests.get('https://imgur.com/search?q=' + photos)
#ensure the request worked
res.raise_for_status()

#step 3
#create the Beautiful Soup object for the request
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#select all <img> elements
imgElems = soup.select('img')
#check if anything was returned
if imgElems == []:
    #print out that no images were found
    print('No images foundfor search: ' + photos)
else:   
    #now do not open and files that do not end with .jpg
    for img in imgElems:
        if not img.get('src').endswith('.jpg'):
            imgElems.remove(img)

#step 4
#loop through all of the images in imgElems
for img in imgElems:
    #create the url for the image found in imgElems using get, getting the value at 'alt src'
    imgUrl = 'https:' + img.get('src')
    #output what is being downloaded
    print('Downloading image %s...' % imgUrl)
    #use requests to download the url for the img
    res = requests.get(imgUrl)
    #ensure the request worked
    res.raise_for_status()
    
    #open the imagefile, use the base name of the imgUrl to save as a .jpg
    imageFile = open(os.path.join('imgur_downloads', os.path.basename(imgUrl)), 'wb')
    #use iter_content to download the photos
    for chunk in res.iter_content(100000):
        #write the image to the file
        imageFile.write(chunk)
        
    #close the imageFile
    imageFile.close
    
#print when the program has completed
print('Done!')
    

