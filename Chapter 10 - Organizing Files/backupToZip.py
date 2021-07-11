#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:38:30 2021

@author: paulmason
program that takes the current directory and compresses it into a zip file
is meant to take 'snapshots' of the current directory so program can be run multiple times
each time will append a number to the name of the zip file
once file is run will create a zipfile for all of the Chapter 10 content, as many times
as the user runs it for multiple different snapshots of the directory
"""

#import the necessary libraries
#zipfile for the zipfile function to compress the folder and os for path functions
import zipfile, os

#backup the contents of folder to a zip file
def backupToZip(folder):
    #ensure folder is absolute with abspath
    folder = os.path.abspath(folder)
    
    #figure out the filename based on the files that already exist
    number = 1
    
    #loop runs once as it makes the filename for the zipfile
    while True:
        #make the filename for the zip file
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        
        #then immediately break out of the loop to avoid an infinite loop
        if not os.path.exists(zipFileName):
            break
        
        #append number to be able to run the program multiple times
        number += 1
        
    #create the zip file
    #printout the name of the zipfile that will be created
    print(f'Create file {zipFileName}')
    #call ZipFile() to actually create the ZipFile and create it in write mode
    backup = zipfile.ZipFile(zipFileName, 'w')
   
    #walk the entire folder tree and compress files into each folder
    for folderName, subFolders, fileNames in os.walk(folder):
        #print out the files being added to folderName
        print(f'Adding files to {folderName}')
        #add the current folder to the zip file
        backup.write(folderName)
        
        #add all files in foldername to backup
        for fileName in fileNames:
            newBase = os.path.basename(folder) + '_'
            #have a check to make sure you do not backup the backup zip folders
            if fileName.startswith(newBase) and fileName.endswith('.zip'):
                continue
            #write backup to folder
            backup.write(os.path.join(folderName, fileName))
            
    #close the backup zip file
    backup.close()
    #tell the user the program is done running 
    print("Done.")

#call backupToZip on the current directory
backupToZip('.')     

