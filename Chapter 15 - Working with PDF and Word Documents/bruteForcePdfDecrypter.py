#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bruteForcePdfDecrypter.py
Created on Sun Aug  8 23:10:38 2021

@author: paulmason

program that uses the brute-force method to decrypt an encrypted PDF given by the user
program should try both the uppercase and lowercase version of each word and give the password
when/if a word in the txt file successfully decrypts the PDF file

steps:
    1. get an encrypted PDF file from the user and create a PdfFileReader object and ensure it is encrypted
    2. read in dictionary.txt and loop through all words in it (uppercased) and a copied list in lowercase
       if the decrypt() method returns 1 then print the password and end the program
    3. else then the encrypted PDF cannot be decrypted with the bruteforce method and the user should be told that
"""

#import PyPDF2 to attempt to decrypt the encrypted file given and sys to exit the program if needed
import PyPDF2, sys

#step 1 - get the encrypted PDF from the user
#create an object to store the PDF in
pdfFile = ''
#prompt user to enter an encrypted pdf
while not pdfFile.endswith('.pdf'):
    print('Enter an encrypted PDF file:')
    pdfFile = input()
    
#create a PdfFileReader object from the PDF file given
pdfReader = PyPDF2.PdfFileReader(open(pdfFile, 'rb'))

#ensure the PDF file is encrypted
if not pdfReader.isEncrypted:
    #tell the user they entered a PDF that is not encrypted and exit
    print('User entered a PDF file that is not decrypted! Program terminating...')
    sys.exit()
    
#step 2 - read in the values from dictionary.txt
#open the file for dictionary.txt
dictFile = open('dictionary.txt', 'r')
#use readlines to make a list for each word in the file
passwordWords = dictFile.readlines()
#output what is happening
print('Creating lowercase words list...')
#now create a lowercased list of passwordsWords
lcPasswordWords = [x.lower() for x in passwordWords]

#while passWords is False loop through both upper and lowercase password lists
while True:
    
    #loop through the lowercase words
    for word in lcPasswordWords:
        #strip all blank spaces
        word = word.strip()
        #print what word is being attempted to decrypt
        print('Attempting with %s...' % word)
        #check if the word decrypts the PDF
        if pdfReader.decrypt(word):
            #then print out the password
            print('Success! The password for %s is %s!' % (pdfFile, word))
            #set break out
            sys.exit()
    
    #loop through uppercase words
    for word in passwordWords:
        #strip all blank spaces
        word = word.strip()
        #print what word is being attempted to decrypt
        print('Attempting with %s...' % word)
        #check if the password decrypts the PDF
        if pdfReader.decrypt(word) == 1:
            #if so print out the password
            print('Success! The password for %s is %s!' % (pdfFile, word))
            #then break out
            sys.exit()
    
    #if you have looped through both lists and arrive here, then the password is not in dictionary.txt
    print('Unfortunately, dictionary.txt does not hold the password for %s. Program terminating...' % (pdfFile))
    sys.exit()

