#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdfParanoiaEncryption.py
run program on mac: python3 pdfParanoiaEncryption.py <PASSWORD>
Created on Wed Aug  4 18:19:25 2021

@author: paulmason

program that finds all non-encrpted PDFs in the current wordking directory and encrypts them with the
password entered on the command line

steps:
    1. check that a second argument, the password, was given on the cmd line and quit if not
    2. loop through all files in the cwd that end in .pdf and are not encrypted
    3. encrypt all of those files with the password entered on the command line
    4. save the new encrypted PdfFileWriter object and delete the file used to create the PdfFileReader object
"""

#import PyPDF2 to open PDF files and create new encrypted PDF files and os to get files in the cwd
#and finally sys to check the amount of arguments on the cmd line
import PyPDF2, os, sys

#step 1 - check that a password was entered
#if password was enetered there will be 2 cmd line arguments entered
if len(sys.argv) == 2:
    #set the password to the second argument on hte cmd line
    password = sys.argv[1]
else:
    #then a password was not entered or it was too long
    print('Either no password entered or password cannot be multiple words!')
    #quit the program
    sys.exit()
    
#tell the user what the program does
print('This program encrypts all PDF files in the current working directory with the password %s.' % password)

#step 2 - loop through all non-encrypted PF files
#create an empty list to store the PDF files in 
pdfFiles = []
#loop through all the files in the cwd
for file in os.listdir('.'):
    #ensure file ends with .pdf
    if file.endswith('.pdf'):
        #append the file to the list of PDF files
        pdfFiles.append(file)
        
#ensure there are PDF files in the cwd
if len(pdfFiles) == 0:
    #output there are no PDF files in the cwd
    print('There are no PDFs in the cwd!')
    #quit the program
    sys.exit()
        
#loop through all the files in the list of PDF files
for fileName in pdfFiles:
    #create a file object for the PDF file
    #pdfFileObj = open(fileName, 'rb')
    #create a PdfFileReader object from the file object
    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfReader = PyPDF2.PdfFileReader(open(fileName, 'rb'))
    
    #now only continue if the file is not encrypted
    if not pdfReader.isEncrypted:
        #if not create a PdfFileWriter object
        pdfWriter = PyPDF2.PdfFileWriter()
        
        #loop through all the pages in the PdfFileReader object
        for pageNum in range(pdfReader.numPages):
            #create a page object for the current page
            pageObj = pdfReader.getPage(pageNum)
            #add the page to the PdfFileWriter object
            pdfWriter.addPage(pageObj)
        
        #step 3 - encrypt the file with the password given
        pdfWriter.encrypt(password)
        
        #step 4 - save the new PDF file and delete the old one
        #create a new filename by added encrypted to it
        encryptedFileName = fileName.replace('.pdf', '_encrypted.pdf')
        #open the encrypted file in write binary mode
        encryptedFileObj = open(encryptedFileName, 'wb')
        #output what file is being encrypted
        print('Saving encrypted file: %s...' % encryptedFileName)
        #write the PdfFileWriter object to the encrypted file
        pdfWriter.write(encryptedFileObj)
        #close the encrypted file 
        encryptedFileObj.close()
        #output to user what file is being deleted
        print('Deleting file: %s...' % fileName)
        #remove the old decrypted PDF file
        os.remove(fileName)
    #close the PdfFileReader object
    #pdfFileObj.close()
        
#output that the program is done
print('Done!')
        