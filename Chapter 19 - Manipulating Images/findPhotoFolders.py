#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
findPhotoFolders.py
Created on Sat Aug 28 01:16:18 2021

@author: paulmason

a program that searches for photo folders on your hard drive
a photo folder is defined as having at least half of the files in the folder as a photo
and each photo must have a width and height greater than 500 to count as a photo

steps:
    1. go through all of the folders on your hard drive
    2. count all of the non photo files
    3. get the photo dimensions and determine if it should count as a photo or not
    4. print out the absolute path of the photo folder
"""
#import the Image module from Pillow to get the photo dimensions
from PIL import Image
#import os to walk through all folders on your computer
import os

#step 1 - go through all folders
#this for loop goes through all folders on your machine with the argument / given to walk
for foldername, subfolders, filenames in os.walk('/'):
    #create variables to keep track of how many photos and non photos the folder contains
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    #step 2 - count all non photo files
    for filename in filenames:
        #check if file extension isn't .png or .jpg
        #also certain files were causing issues leading to  the extra conditionals after the png and jpg one
        if not (filename.endswith('.png') or filename.endswith('.jpg')) or foldername.endswith('ipptool') or filename.endswith('@2x.png') or ('.gradle' in foldername) or ('MATLAB_R2020b.app' in foldername):
            numNonPhotoFiles += 1
            continue    # skip to next filename

        #step 3 - get photo dimensions and determine if it should count as a photo
        #print('opening image %s...' % os.path.join(foldername, filename))
        #open image file using Pillow.
        im = Image.open(os.path.join(foldername, filename))
        #get the dimensions of the photo
        width, height = im.size

        #check if width & height are larger than 500
        if width > 500 and height > 500:
            #image is large enough to be considered a photo
            numPhotoFiles += 1
        else:
            #image is too small to be a photo
            numNonPhotoFiles += 1

    #step 4 - print out the absolute path of the photo folder
    #if more than half of files were photos,
    #print the absolute path of the folder.
    if numPhotoFiles > numNonPhotoFiles:
        print('Photo folder path: %s' % os.path.join(foldername))
        print()
        
print('Done.')
        
        