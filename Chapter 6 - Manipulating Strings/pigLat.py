#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 17:48:15 2021

@author: paulmason
"""
#program that converts english to pig latin
#rules:
    #if word begins with vowel, then 'yay' is added to the end of it
    #if word begins with consonant or consonant cluster then that is moved to the end of the 
    #word followed by 'ay'

#prompt the user
print('Enter a message in English to be translated to Pig Latin.')
#get the message from input()
message = input()

#keep a constant tuple value to store all vowels (and y)
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

#create an empty list to hold the Pig Latin words as they are translated
pigLatin = []

#loop through the message by each word entered
for word in message.split():
    #separate the non-letters at the start of each row
    prefixNonLetters = ''
    
    #loop through the word while it has characters in it and the first char isn't a letter
    while len(word) > 0 and not word[0].isalpha():
        #add the non letter character to prefixNonLetters
        prefixNonLetters += word[0]
        #reset the word with the non letter character removed
        word = word[1:]
        
    if len(word) == 0:
        #add prefixNonLetters to pigLatin when the length of word is 0
        #this is cause the whole string contains non letter characters
        pigLatin.append(prefixNonLetters)
        #go onto the next word
        continue
    
    #separate the nonletters at the end of the word
    suffixNonLetters = ''
    
    #now loop through the end of the word string checking for non letter characters
    while not word[-1].isalpha():
        #add the nonletter to suffixNonLetters
        suffixNonLetters += word[-1]
        #create the new word without the non letter characters
        word = word[:-1]
    
    #remember if the word was in upper or title case
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    
    #make the word lower case for translation
    word = word.lower()
    
    #separate the consonants at the start of the word
    prefixConsonants = ''
    
    #loop until either the first char is a vowel or the word's length is 0
    while len(word) > 0 and not word[0] in VOWELS:
        #add the consonants to prefixConsonants
        prefixConsonants += word[0]
        #recreate the word with the consonant removed
        word = word[1:]
    
    #add the Pig Latin ending to the word
    if prefixConsonants != '':
        #add the ending for words that begin with consonants
        word += prefixConsonants + 'ay'
    else:
        #add the ending for words that begin with vowels
        word += prefixConsonants + 'yay'
    
    #reset the word to upper or title case if it was in that before
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    
    #add the non letters to the start or end of the word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

#join all the words back together into a single string
print(' '.join(pigLatin))