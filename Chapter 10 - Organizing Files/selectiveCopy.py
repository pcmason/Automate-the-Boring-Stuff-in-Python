#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:13:45 2021

@author: paulmason
file that goes through all files in the current directory and 
copies all files that end in .txt
for the Github stuff, I will still use the 10-30-1998file.txt which will have a copy
created in a folder titled 'spam' in your home directory
"""

#import the os (for path) and shutil (for copy) modules
import os, shutil
#import Path from Pathlib for shutil.copy
from pathlib import Path

#create the function so selective copy can be run on any folder
def selectiveCopy(folder):
    #ensure the folder is absolute
    folder = os.path.abspath(folder)
    
    #walk over the entire folder tree searching for folders ending in .txt
    for folderName, subFolders, fileNames in os.walk(folder):
        #print out the name of the current folder
        print(f'The current folder is: {folderName}')
        
        #go through the files in the folder to see if they end in .txt
        for fileName in fileNames:
            if fileName.endswith('.txt'):
                #print the file being copied
                print(f'Copying: {fileName}')
                #copy the file to spam, which will be in your home directory
                shutil.copy(os.path.join(folderName, fileName), Path.home() / 'spam')
                
    #tell the user the program has completed running 
    print('Done.')
    
#run the function on the current directory
selectiveCopy('.')
            
    
    