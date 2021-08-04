#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
combinedPdfs.py
Created on Mon Aug  2 20:13:19 2021

@author: paulmason

program that combines all PDFs in the current working directory into a single PDF

steps:
    1. find all PDF files in the cwd
    2. open each PDF file found
    3. add each page to the PdfFileWriter object, except the first page of each PDF in the cwd
    4. save the result to a new PDF titled 'allminutes'
"""

#import PyPDF2 to read in all the pdf files in the cwd and to add their pages to a new PDF file
#import os to get the current working directory
import PyPDF2, os

#step 1 - get all the PDF filenames
#create an empyt list to store the PDF files in
pdfFiles = []

#use the listdir method from os to get all files in the cwd
for file in os.listdir('.'):
    #check that the file ends with the .pdf extension
    if file.endswith('.pdf'):
        #if so add it to the list of PDF files
        pdfFiles.append(file)
        
#sort the PDFs in alphabetical order, not worrying about case
pdfFiles.sort(key = str.lower)
#create a PdfFileWriter to hold the combined PDF files pages (minus their cover)
pdfWriter = PyPDF2.PdfFileWriter()

#step 2 - read each file in the list of PDF files found

#loop through all the PDF files
for fileName in pdfFiles:
    #open the PDF file in read-binary mode
    pdfFileObj = open(fileName, 'rb')
    #create a PdfFileReader object for each PDF file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    #step 3 - add each page (minus first one) from PdfFileReader obj to the PdfFileWriter obj
    #start for loop at 1 to skip the first page
    for pageNum in range(1, pdfReader.numPages):
        #get the Page object
        pageObj = pdfReader.getPage(pageNum)
        #add the Page object to the PdfFileWriter object
        pdfWriter.addPage(pageObj)
        
#step 4 - save the results to a new pdf
#save the file with title 'allminutes'
resultFile = open('allminutes.pdf', 'wb')
#write the content of the PdfFileWriter object to the result file
pdfWriter.write(resultFile)
#close the result file
resultFile.close()
