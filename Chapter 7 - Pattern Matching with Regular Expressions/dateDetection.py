#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:27:33 2021

@author: paulmason
program that detects valid dates in the format of DD/MM/YYYY
"""
#first import the regex module
import re

#create the date regex
dateRegex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
#search for a regex object 
mo = dateRegex.search('31/06/2304')
#create an example for a correct leap year
leapYear = dateRegex.search('29/02/2400')
#create an incorrect example
unrealDay = dateRegex.search('29/02/2015')
#print the found regex date
#print(mo.group())

#create a list for each date
dates = [mo, leapYear, unrealDay]

#create function to check if the date is valid
def validDate(d, m, y):
    #if there are more than 31 days or less than 1 days this is not valid
    if d < 1 or d > 31:
        return False
    
    #if there are more than 12 months or less than 1 month than this is not valid
    if m < 1 or m > 12:
        return False
    
    #year is between 1000 to 2999
    if y < 1000 or y > 2999:
        return False
    
    #April June September and November have only 30 days
    if (m == 4 or 6 or 9 or 11) and (d > 30):
            return False
        
    #February has 28 days except during leap years
    if m == 2 and y % 4 == 0 and (y % 400 == 0 or y % 100 != 0):
        #a leap year
        if d > 29:
            return False
    elif m == 2 and (y % 4 != 0 or y % 100 == 0):
        #not a leap year
        if d > 28:
            return False
        
    #if made it this far return true
    return True

#call validDate on day, month and year
#assign the groups to variable they represent by looping through dates
for date in dates:
    day = int(date.group(1))
    month = int(date.group(2))
    year = int(date.group(3))
    
    #debug printout, useful to see each group
    #print(day)
    #print(month)
    #print(year)
    
    #call validDate in the print statement below to determine if the date is valid (results: F, T, F)
    print('The date\'s ' + date.group() + ' validity is: ' + str(validDate(day, month, year)))
    

