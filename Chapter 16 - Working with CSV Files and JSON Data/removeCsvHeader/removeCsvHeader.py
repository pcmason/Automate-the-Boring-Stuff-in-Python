#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
removeCsvHeader.py
Created on Tue Aug 10 20:28:57 2021

@author: paulmason

program that goes through all of the CSV files in the current working directory 
and removes the header from those files and saves the new, header-less, CSV file

steps:
    1. loop over a list of files from os.listdir(), skipping the non CSV files
    2. create a CSV reader object and read in the contents of the file, using line_num
       to know which line to skip
    3. create a CSV writer object and write out the read-in data to a new file
"""

#import csv to create reader and writer objects and os to get the files in the cwd
import csv, os

#create a file for all of the CSV files with headers removed
os.makedirs('headerRemoved', exist_ok = True)

#step 1 - loop through each CSV file
#loop through all files in the cwd
for csvFilename in os.listdir('.'):
    
    if not csvFilename.endswith('.csv'):
        #skip non csv files
        continue
    
    #output to user what CSV file the program is removing the header from
    print('Removing header from %s...' % csvFilename)
    
    #step 2 - read-in the CSV file
    #create list to store the content of the CSV file
    csvRows = []
    #open CSV file
    csvFileObj = open(csvFilename)
    #create reader object
    csvReader = csv.reader(csvFileObj)
    
    #loop through the rows of the CSV file
    for row in csvReader:
        
        if csvReader.line_num == 1:
            #skip the header row
            continue
        
        #otherwise append the content to csvRows
        csvRows.append(row)
        
    #close the CSV file
    csvFileObj.close()

    #step 3 - write out the headerless CSV file
    #open a new file added to the headerRemoved dir for the headerless CSV file
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline = '')
    #create the writer object
    csvWriter = csv.writer(csvFileObj)
    
    #loop through the saved rows from the reader object
    for row in csvRows:
        #write them to the writer
        csvWriter.writerow(row)
    
    #close the writer file
    csvFileObj.close()
    
#output the completion of the program
print('Done!')

