#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:24:36 2021

@author: paulmason
"""
#program that takes a list of list of strings and displays it in an organized table with each 
#column right adjusted

#use np.array from numpy
import numpy as np

#define the printTable function
def printTable(table):
    #create an empty list with as many 0's as inner lists in table
    colWidths = [0] * len(table)
    
    #now loop through table to find the largest word in each column
    for i in range(len(table)):
        for j in range(len(table[i])):
            
            #check if the word is larger than the value in colWidths
            if len(table[i][j]) > int(colWidths[i]):
                #reassign the max value in colWidths
                colWidths[i] = len(table[i][j])
                
    #transpose the table before printing
    table = table.T
    
    #now print the values in table based on the colWidths
    for i in range(len(table)):
        for j in range(len(table[i])):
            
            print(table[i][j].rjust(colWidths[j]), end = ' ')
            
        #print a newline
        print()
    
#example table 
tableData = np.array([['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']])

#call printTable on tableData
printTable(tableData)