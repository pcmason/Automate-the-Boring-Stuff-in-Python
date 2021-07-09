#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 22:12:38 2021

@author: paulmason
"""
#write a function that takes a list and returns a string with the values in the list
#these values should be separated by a ',' with the last item separated by 'and'

#method takes a list as its only parameter
def commaCode(listVar):
    #if an empty list is passed to the function return ''
    if listVar == []:
        return ''
    #string that will be created from list
    compressedList = ''
    #loop through values in list given
    for i in range(len(listVar) - 1):
        #append the word in the list to the string
        compressedList += listVar[i]
        #this element is not the last element so use a comma to separate the strings
        if i < len(listVar) - 2:
            #then append a comma
            compressedList += ', '
        #else this is the last value so use the word and instead
        else:
            #then add 'and'
            compressedList += ' and ' + str(listVar[i + 1])
    #return the string
    return compressedList

#create a test list
spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['apples', 'bananas', 'tofu', 'cats', 'cows', 'cowboys', 'cities', 'programmers', 'fun']

#call commaCode on spam
print(commaCode(spam))
#also call it on spam2, a longer example
print(commaCode(spam2))
