#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 04:54:11 2021

@author: paulmason
program to generate 35 random quizzes and their associated answer keys with 50 questions
"""

#import random to randomly generate the quizzes
import random

#quiz data: keys are states and values are the capital
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
   'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 
   'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
 
#decide number of quizzes to generate
NUMQUIZZES = 35
    
#generate quiz files
for quizNum in range(NUMQUIZZES):
    #create the quiz and answer key files
    #to make each file unique add the quizNum + 1 to the end of the filename, add writing capabilities
    quizFile = open(f'/Users/paulmason/Desktop/Automate_Boring_Stuff/quizzes/capitalsquiz{quizNum + 1}.txt', 'w')
    #create answer key file
    answerKeyFile = open(f'/Users/paulmason/Desktop/Automate_Boring_Stuff/answerkeys/capitalsquiz_answers{quizNum + 1}.txt', 'w')

    #write out the header for the quiz
    #header gives student lines to enter name, date and period
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    #write the title of the quiz
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form {quizNum + 1})')
    quizFile.write('\n\n')
    
    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)
    
    #loop through all 50 states, making a question for each
    for questNum in range(50):
        #get the right answers
        rightAnswer = capitals[states[questNum]]
        #get all values in capitals
        wrongAnswers = list(capitals.values())
        #delete the correct answer in wrongAnswers
        del wrongAnswers[wrongAnswers.index(rightAnswer)]
        #select three random values from wrongAnswers using random.sample()
        wrongAnswers = random.sample(wrongAnswers, 3)
        #create list of answer options of right answer with 3 wrong answers
        answerOpts = wrongAnswers + [rightAnswer]
        #randomize answerOpts so correct answer is not always D
        random.shuffle(answerOpts)
        
        #write the question and answer options to the quiz file
        quizFile.write(f'{questNum + 1}. What is the capital of {states[questNum]}?\n')
        #write the four answer options
        for opt in range(4):
            #'ABCD'[opt] evaluates ABCD as an array/list
            quizFile.write(f"     {'ABCD'[opt]}. { answerOpts[opt]}\n")
            quizFile.write('\n')
            
        #write the answer key to a file
        answerKeyFile.write(f"{questNum + 1}. {'ABCD'[answerOpts.index(rightAnswer)]} ")
        
    #close the quiz and answer key files
    quizFile.close()
    answerKeyFile.close()
        
        
    
    