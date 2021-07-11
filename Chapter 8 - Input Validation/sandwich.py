#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 02:50:28 2021

@author: paulmason
create a program that asks a user to order a sandwich
"""

#import pyinputplus as many functions from it will be used in this project
import pyinputplus as pyip

#create variable for price, the minimum price is 5 per basic sandwich (just bread and protein)
price = 5

#prompt the user to choose a type of bread
breadPrompt = 'Choose one of the following types of bread:\n'
#user can choose from wheat, white and sourdough
breadResponse = pyip.inputMenu(['wheat', 'white', 'sourdough'], breadPrompt)

#prompt the user to choose a type of protein
protPrompt = 'Choose one of the following proteins:\n'
#user can choose from chicken, turkey, ham or tofu
protResponse = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], protPrompt)

#prompt the user if they want cheese
wantCheese = 'Do you want cheese on your sandwich?\n'
#yes/no response
cheeseResponse = pyip.inputYesNo(wantCheese)

#check if the user wanted cheese
if cheeseResponse == 'yes':
    #prompt the user for what kind of cheese they want
    whichCheese = "Choose one of the following cheeses:\n"
    #cheese options: cheddar, swiss and mozarella
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'], whichCheese)
    #cheese is 50 cents
    price += .5

#ask if they want lettuce
wantLettuce = 'Do you want lettuce on your sandwich?\n'
#yes/no response
lettuceResponse = pyip.inputYesNo(wantLettuce)

if lettuceResponse == 'yes':
    #lettuce costs 50 cents
    price += .5

#ask if they want mayo
wantMayo = 'Do you want mayo on your sandwich?\n'
mayoResponse = pyip.inputYesNo(wantMayo)

if mayoResponse == 'yes':
    #mayo costs 50 cents
    price += .5

#ask if they want ketchup
wantKetchup = 'Do you want ketchup on your sandwich?\n'
ketchupResponse = pyip.inputYesNo(wantKetchup)

if ketchupResponse == 'yes':
    #ketchup costs 50 cents
    price += .5

#ask if they want mustard
wantMustard = 'Do you want mustard on your sandwich?\n'
mustardResponse = pyip.inputYesNo(wantMustard)

if mustardResponse == 'yes':
    #mustard costs 50 cents
    price += .5

#ask how many of these sandwiches they are ordering
numSandwiches = 'How many of these sandwiches will you be ordering?\n'
#user must order at least 1 sandwich with technically no maximum value in place
orderNum = pyip.inputNum(numSandwiches, min = 1)

#multiply price by number of sandwiches ordered
price *= orderNum

#tell the user the cost
print("The total cost is: $%s." % (price))