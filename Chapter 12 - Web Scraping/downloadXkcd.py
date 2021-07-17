#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
downloadXkcd.py
Created on Wed Jul 14 00:07:57 2021

@author: paulmason

as of July 16th 2021 this program will download 2,488 comics, so it takes a few minutes to run!

program opens https://xkcd.com/ a popular geek comic and downloads every comic on the website
start by downloading the first comment then keep hitting the 'previous' button and 
downloading the next comic until there are no more to download

steps:
    1. download pages with the requests module
    2. find the URL of the comic image using bs4
    3. download and save the comic to hard drive using iter_content() method
    4. find URL of previous comic link and repeat until done
"""

#imoprt requests to download the pages, bs4 to specify comics and Previous button
#and os to store the comics on the harddrive
import requests, bs4, os

#starting url for xkcd.com
url = 'https://xkcd.com'
#store comics in /xkcd, which will be created if folder does not exist and will not throw
#an error if the file is already created as well (SO MAKE SURE THIS IS NOT ALREADY A FILE)
os.makedirs('xkcd', exist_ok = True)

#the first comics Previous button links to : https://xkcd.com/#
while not url.endswith('#'):
    #step 1 download the page
    #output what is being downloaded
    print('Downloading page %s...' % url)
    #download the page using the requests module
    res = requests.get(url)
    #ensure the request did not raise an exception
    res.raise_for_status()

    #createthe Beautiful Soup object for the downloaded page to parse the html
    soup = bs4.BeautifulSoup(res.text, 'html.parser')    
    
    #step 2 find the URL of the comic
    #the <img> element for the comic is always in a <div> element with the class comic
    comicElem = soup.select('#comic img')
    #check if the comic was actually found
    if comicElem == []:
        #print out that the comic was not found
        print('Comic could not be found!')
    else:
        #the src of the comic may or may not have //imgs at the start
        if comicElem[0].get('src').startswith('//imgs'):
            #create the url for the comic, getting most of the url from the 'src' attribute in comicElem
            comicUrl = 'https:' + comicElem[0].get('src')
        else:
            #then need to add xkcd.comas well
            comicUrl = 'https://xkcd.com'+ comicElem[0].get('src')
            
        #output what is being downloaded
        print('Downloading image %s...' % comicUrl)
        #use the requests module to download the url for only the comic's image
        res = requests.get(comicUrl)
        #ensure the request worked
        res.raise_for_status()
    
        #step 3 save the image to the /xkcd file
        #open the file for the image giving it the name as last part of the comicUrl
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        #use iter_content to download the image
        for chunk in res.iter_content(100000):
            #write the bytes to the file
            imageFile.write(chunk)
            
        #when done downloading the image close the comic's file
        imageFile.close()
        
    #step 4 get the Previous button's url
    #the CSS selector is an <a> element with the rel attribute set to 'prev'
    prevLink = soup.select('a[rel="prev"]')[0]
    #create the url for the next page and then go to the top of the while loop
    url = 'https://xkcd.com' + prevLink.get('href')

#output that the downloading of comics is done
print('Done.')


