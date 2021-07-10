#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 13:38:32 2021

@author: paulmason
"""
#this program writes a function that displays the inventory for a player in a fantasy game
#also has a function to add items to the player's inventory

#create the function to display the inventory
def displayInventory(inventory):
    #print inventory so the user knows what is displayed
    print("Inventory:")
    #keep track of the total number of items in the inventory
    invTotal = 0
    #loop through the dict pulling the values and keys with items()
    for k, v in inventory.items():
        #print the value followed by the key
        print(str(v) + ' ' + str(k))
        #add the value to the total number of items
        invTotal += int(v)
    #print out the total number of items in the inventory
    print("Total number of items: " + str(invTotal) + '\n')
    
#create function addToInventory that takes a parameter for current inventory and a list
#of items to be added to the inventory
def addToInventory(inventory, loot):
    #loop over the strings in loot
    for item in loot:
        if item in inventory.keys():
            #if an item in loot already exists in inventory then add one to that items value
            inventory[item] += 1
        else:
            #else create a new key and value for that item setting the default value to one
            inventory.setdefault(item, 1)
    return inventory
            
#create the inventory for the fantasy game
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#create a second inventory
inv = {'gold coin': 42, 'rope': 1}

#create loot from  defeated dragon that will be added to the users inventories
#this is a list of strings
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
    
#now call displayInventory with stuff passed in
displayInventory(stuff)

#add the dragonLoot to inv
inv = addToInventory(inv, dragonLoot)
#display inv to see if the above function worked
displayInventory(inv)
