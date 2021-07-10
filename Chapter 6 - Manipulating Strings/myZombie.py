#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 20:31:59 2021

@author: paulmason
"""
#program creates different types of bots that play the zombie dice game online
#a pdf of the rules can be found here: http://www.sjgames.com/dice/zombiedice/img/ZDRules_English.pdf

#first import the zombie dice module
import zombiedice
#import the random module for the random bot
import random

###UNCOMMENT THESE LINES WHEN FIRST RUNNING PROGRAM###
#now call a demo for the first time this program is being run to see how zombiedice works
#zombiedice.demo()

#create a zombie bot that rolls once then randomly decides to keep rolling or not
class myRandZombie:
    def __init__(self, name):
        #zombies must have names
        self.name = name
    
    def turn(self, gameState):
        #zombie must roll once
        diceRollResults = zombiedice.roll()
        #set brains to 0
        brains = 0
        #loop as long as 3 shotguns were not rolled
        while diceRollResults is not None:
            #add the number of brains rolled to brains
            brains += diceRollResults['brains']
            
            if random.randint(0,1) == 0:
                #randomly decided to roll again
                diceRollResults = zombiedice.roll()
            else:
                break
    
#create a zombie bot that stops rolling after it has rolled 2 brains
class myHumbleZombie:
    def __init__(self, name):
        #zombie must have name
        self.name = name
    
    def turn(self, gameState):
        #zombie must roll once
        diceRollResults = zombiedice.roll()
        #set brains to 0
        brains = 0
        #loop as long as 3 shotguns weren't rolled
        while diceRollResults is not None:
            #add the number of brains rolled to brains
            brains += diceRollResults['brains']
            
            if diceRollResults['brains'] == 2:
                #if dice results are exactly 2 brains zombie stops rolling
                break
            else:
                #roll again
                diceRollResults = zombiedice.roll()

#bot that stops rolling if 2 shotguns have been rolled
class myStopAtTwoShotZombie:
    def __init__(self, name):
        #zombie must have name
        self.name = name
    
    def turn(self, gameState):
        #zombie must roll once
        diceRollResults = zombiedice.roll()
        #set brains to 0
        brains = 0
        #loop as long as 3 shotguns weren't rolled
        while diceRollResults is not None:
            #add the number of brains rolled to brains
            brains += diceRollResults['brains']
            
            if (diceRollResults['shotgun'] == 2):
                #if 2 shotguns have been rolled the zombie stops rolling
                break
            else:
                #roll again
                diceRollResults = zombiedice.roll()

#bot that rolls randomly 1-4 times or stops if 2 shotguns are rolled
class riskAverseZombie:
    def __init__(self, name):
        #zombie must have name
        self.name = name
    
    def turn(self, gameState):
        #zombie must roll once
        diceRollResults = zombiedice.roll()
        #set brains to 0
        brains = 0
        #decide randomly to roll 1-4 times
        numRolls = random.randint(1,4)
        #create a counter to keep track of how many rolls have occured
        count = 0
        #loop as long as 3 shotguns weren't rolled and have not rolled the random amount determined above
        while diceRollResults is not None and count < numRolls:
            #add the number of brains rolled to brains
            brains += diceRollResults['brains']
            
            if diceRollResults['shotgun'] == 2:
                #if 2 shotguns have been rolled the zombie stops rolling
                break
            else:
                #add to the counter
                count += 1
                #roll again
                diceRollResults = zombiedice.roll()
                
#bot that stops rolling after it has more shotguns than brains
class moreShotThanBrain:
    def __init__(self, name):
        #zombie must have name
        self.name = name
    
    def turn(self, gameState):
        #zombie must roll once
        diceRollResults = zombiedice.roll()
        #set brains to 0
        brains = 0
        #loop as long as 3 shotguns weren't rolled
        while diceRollResults is not None:
            #add the number of brains rolled to brains
            brains += diceRollResults['brains']
            
            if diceRollResults['shotgun'] > diceRollResults['brains']:
                #if more shotguns than brains rolled then stop rolling
                break
            else:
                #roll again
                diceRollResults = zombiedice.roll()
             
                
#here are the zombies that have been created above in action
#comments explain the names for the zombies
#all of my bots created above begin with 'M'
zombies = (
    #R: Random
    zombiedice.examples.RandomCoinFlipZombie(name='R'),
    #MR: My Random
    myRandZombie(name = "MR"),
    #MH: My Humble
    myHumbleZombie(name = "MH"),
    #UL: Until Leading
    zombiedice.examples.RollsUntilInTheLeadZombie(name='UL'),
    #SATS: Stops At Two Shotguns
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='SATS', minShotguns=2),
    #MSATS: My Stops At Two Shotguns
    myStopAtTwoShotZombie(name = "MSATS"),
    #MRA: My Risk Averse
    riskAverseZombie(name = "MRA"),
    #MSTB: More Shotguns than Brains
    moreShotThanBrain(name ="MSTB"),
    #SAOS: Stops At One Shotgun
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='SAOS', minShotguns=1),
    #MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)