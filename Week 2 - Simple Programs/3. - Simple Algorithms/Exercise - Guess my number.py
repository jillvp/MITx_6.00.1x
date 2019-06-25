#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:55:56 2019

@author: Ignite303
"""


#low = 0
#high = 100
#
##ans = (high + low)//2
#
#x = int(input('Please think of a number between 0 and 100'))
#
#while True:
#    guess = (high + low)//2
#    
#    print('Is your secret number ' + str(guess) + '?',end=' ')

#print("Enter 'h'to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

#    response = input("Enter 'h'to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#    response = str(response)

# when user enters something invalid:

#    while response not in ['h', 'c', 'l']:
#        print("Sorry, I did not understand your input.",end=' ')
#        print('Is your secret number ' + str(ans) + '?',end=' ')
#        response = input("Enter 'h'to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#        response = str(input("))

# subsequent guesses        
#    if response == 'c':
#        break
#    
#    if response == 'l':
#        low = ans
#    else:
#        high = anw
#    ans = (high + low)//2

#while response != 'c':
#    if response == 'h':
#        high = ans
#        ans = (high + low)//2
#        print('Is your secret number ' + str(ans) + '?',end=' ')
#        response = input("Enter 'h'to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#        response = str(response)
#        
#    if response == 'l':
#        low = ans
#        ans = (high + low)//2
#        print('Is your secret number ' + str(ans) + '?',end=' ')
#        response = input("Enter 'h'to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
#        response = str(response)
#        
#    if response == 'h':

# while
    
# -------------
    
print("Please think of a number between 0 and 100!")

low = 0
high = 100


#x = int(input('Please think of a number between 0 and 100')) -- no INPUT REQUIRED!

while True:
    guess = (high + low)//2
    print('Is your secret number ' + str(guess) + ' ?')
    a = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if a == 'c':
        print('Game over. Your secret number was:', str(guess))
        break
    elif a == 'l':
        low = guess
    elif a == 'h':
        high = guess
    else:
        print('Sorry, I did not understand your input.')