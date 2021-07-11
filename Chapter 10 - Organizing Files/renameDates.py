#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:24:52 2021

@author: paulmason
renames filenames from American style (MM-DD-YYYY) to European style (DD-MM-YYYY)
there is an example file in this folder: 10-30-1998file.txt that after running this program will
be renamed to 30-10-1998file.txt
"""

#import necessary libraries
#import shutil for shutil.move() that can rename files
#import re for re.compile() to create a regex pattern to match American style dates
#import os for os.listdir() which lists all files and folders in the current directory
import shutil, os, re

#create a REGEX pattern to match American style dates
#re.VERBOSE allows whitespace and comments in the REGEX pattern
datePattern = re.compile(r"""^(.*?)      #all text before date
                         ((0|1)?\d)-     #one or two numbers for month
                         ((0|1|2|3)?\d)- #one or two numbers for day
                         ((19|20)\d\d)   #four numbers for year
                         (.*?)$          #all text after date
                         """, re.VERBOSE)
                         
#loop over the files in the working directory
for amerFilename in os.listdir('.'):
    #check if any files have the American style dates
    mo = datePattern.search(amerFilename)

    #skip files without a date
    if mo == None:
        continue

    #get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    #form the European style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    #get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    #rename the files
    print(f'Renaming "{amerFilename}" to  "{euroFilename}"...')
    shutil.move(amerFilename, euroFilename)

