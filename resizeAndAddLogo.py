#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
resizeAndAddLogo.py
Created on Tue Aug 24 19:44:48 2021

@author: paulmason

program that resizes images in the directory and adds a small logo watermark to the corner for each image
all images should be resized to be a 300X300 square

modified to work with gif and bmp images as well, also modofied to be case-insensitive
finally ensure that the photo's height and width are at least twice the size of the watermark's to add it

steps:
    1. open the logo image
    2. loop over all files and open images
    3. resize the images
    4. add the logo and save the changes
"""
#import os to get all the images in the cwd
import os
#import Pillow to create, resize and paste the watermark to images
from PIL import Image

#step 1 - open the logo image
#set constants to change if you want to change how the program runs, constants for resizing images and logo file
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

#open the logo image
logoIm = Image.open(LOGO_FILENAME)
#the logo image is wayyyyy too big so resize to be a 50, 50 image
logoIm = logoIm.resize((50, 50))
#get the width and height of the logo image
logoWidth, logoHeight = logoIm.size

#steo 2 - loop over all files and open images
#loop over all files in the cwd
for filename in os.listdir('.'):
    #do not open any files that do not end in .png or .jpg or is the logo image itself
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.PNG') or filename.endswith('.JPG') or filename.endswith('.gif') or filename.endswith('.bmp')) or filename == LOGO_FILENAME:
        continue
    
    #otherwise open the image object and get its width and height
    im = Image.open(filename)
    width, height = im.size
    
    #step 3 - resize the images
    #check if the image needs to be resized
    if width > SQUARE_FIT_SIZE or height > SQUARE_FIT_SIZE:
        #calculate the new width and height to resize to
        if width > height:
            #height should be reduced by the same proportion width will be reduced by
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            #width should be reduced by the same proportion height will be reduced by
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
          
        #resize the image
        print('resizing %s...' % filename)
        #resize the image with the new width and height determined by the conditional above
        im = im.resize((width, height))

    #step 4 - add the logo and save changes
    #ensure the photo width and height are 2 times greater than the logo's
    if width > 2 * logoWidth and height > 2 * logoHeight:
        #add the logo
        print('Adding logo to %s...' % filename)
        #use the past method to paste the logo to the bottom left corner of the image
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        #save changes to a directory called withLogo
        im.save(os.path.join('withLogo', filename))
    else:
        print('Cannot add logo to %s because file is too small.' % filename)
    
    
    
    
    