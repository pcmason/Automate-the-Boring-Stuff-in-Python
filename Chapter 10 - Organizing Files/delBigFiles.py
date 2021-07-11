#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 04:44:28 2021

@author: paulmason
program that walks through a folder tree and searches for exceptionally large 
files or folders (greater than 100MB) and print the files with their absolute paths
"""

#import the os module for walk(), getsize() and join() functions
import os


#create function so this can be run on any folder/directory
def delBigFiles(folder):
    #ensure the folder's path is absolute
    folder = os.path.abspath(folder)
    
    #walk through the folder
    for folderName, subFolders, fileNames in os.walk(folder):
        #print out the name of the current folder DEBUG UNCOMMENT IF HAVING ISSUES
        #print(f'The current folder is: {folderName}')
        
        #loop through the files in the folder
        for fileName in fileNames:
            #create the path for the filename
            filePath = os.path.join(folderName, fileName)
            #check if the size of the file is greater than 100MB
            #100MB == 100,000 bytes
            size = os.path.getsize(filePath) / 1000
            
            #check if file/folder is greater than 100MB
            if size > 100:
                #print out the file, size and absolute path
                print(f'File: {fileName} is {size} megabytes')
                #print out the absolute path of the file
                print(f'Absolute path for {fileName}: {filePath}')
                
    #print that the function is done
    print('Complete')
    
#call the function on the desktop directory, this is specifically for mac
delBigFiles(os.path.join(os.path.join(os.path.expanduser('~')), "Desktop"))

#for Windows
#delBigFiles(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))