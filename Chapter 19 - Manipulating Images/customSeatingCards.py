#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
customSeatingCards.py
Created on Mon Aug 30 15:45:32 2021

@author: paulmason

program that goes through the guests.txt file and creates custom seating cards for each guest

steps:
    1. open the guests.txt file and card image
    2. create a customized seating card for each guest
    3. save the custom seating card in a file called seatingCards
"""
#import the Image and ImageDraw and ImageFont from Pillow to write out the guests name to the card
from PIL import Image, ImageDraw, ImageFont
#import os to save the custom card to the file in the current directory
import os

#step 1 - open guests.txt and the card image (a pink flower)
guestFile = open('guests.txt', 'r')
guests = guestFile.readlines()

#open the image file
flowerIm = Image.open('flower.jpg')

#create a directory to store the seating cards in
os.makedirs('seatingCards', exist_ok = True)

#step 2 - create a custom card for each guest
#loop through the guests
for guest in guests:
    #create a copy of the flower image
    seatCard = flowerIm.copy()
    #get the width and height of the card
    cardWidth, cardHeight = seatCard.size
    #create the ImageDraw object to draw the text onto the seating card
    draw = ImageDraw.Draw(seatCard)
    #create the arial font using the ImageFont truetype method
    arialFont = ImageFont.truetype(os.path.join('/Library/Fonts', 'arial.ttf'), 100)
    #draw the text of the guest's name in the middle of the card
    draw.text((cardWidth / 4, cardHeight / 2), guest, fill = 'black', font = arialFont)
    
    #step 4 -  save the custom seating card
    #save the file in the folder called seatingCards
    seatCard.save(os.path.join('seatingCards', guest + 'card.jpg'))
    
    
