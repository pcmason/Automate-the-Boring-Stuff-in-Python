#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
threadedDownloadXkcd.py
Created on Mon Aug 16 21:49:53 2021

@author: paulmason

recreates the downloadXkcd.py program from chapter 12 but now uses multiple threads to speed up
the process this has some threads downloading comics while others are establishing connections
and writing the comics to your disk

steps:
    1. create a function to call to download the Xkcd comics, with parameters for start and end comics
    2. create and start running the multiple different threads
    3. wait for all of the threads to end
"""
#import threading for multiple threads, os to make and save the comics to a file on your disk,
#requests to establish a connection with xkcd and bs4 to get the comic image from each page
import threading, os, requests, bs4

#store comics in the CD with extension /xkcd
os.makedirs('xkcd', exist_ok = True)

#step 1 - create a function to download a specific number of Xkcd comics, which are numbered on the site
def downloadXkcd(startComic, endComic):
    
    #loop through specified range of comics
    for urlNumber in range(startComic, endComic):
        #download the page
        print('Downloading page https://xkcd.com/%s...' % urlNumber)
        res = requests.get('https://xkcd.com/%s'% urlNumber)
        #ensure there was no error with the request
        res.raise_for_status()
        
        #create the BeautifulSoup object from the request
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        
        #find the URL of the comic image, it is in elements with id comic with an img tag in it
        comicElem = soup.select('#comic img')
        
        #ensure there was an image there
        if comicElem == []:
            print('Coult not find comic image!')
        else:
            #get the URL of the comic image
            comicUrl = comicElem[0].get('src')
            #download the image
            print('Downloading image %s...' % comicUrl)
            res = requests.get('https:' + comicUrl)
            #ensure request worked
            res.raise_for_status()
            
            #save to image to the created /xkcd folder
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            
            #write the image to the file
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                
            imageFile.close()
            
#step 2 - create and start multiple threads
#a list of all the Thread objects
downloadThreads = []

#loop 14 times to create 14 threads
for i in range(0, 140, 10):
    start = i
    end = i + 9
    
    #no comic at 0 so start at 1
    if start == 0:
        start = 1
    
    #create a thread for downloading 10 Xkcd comics
    downloadThread = threading.Thread(target = downloadXkcd, args = (start, end))
    #append the thread to the list of threads
    downloadThreads.append(downloadThread)
    #start running the new thread
    downloadThread.start()
    
#step 3 - wait for the threads to end
#loop through all the threads in the list
for downloadThread in downloadThreads:
    #the join method ensures the thread has finished
    downloadThread.join()

#then the program is over
print('Done.')
            
            
            
