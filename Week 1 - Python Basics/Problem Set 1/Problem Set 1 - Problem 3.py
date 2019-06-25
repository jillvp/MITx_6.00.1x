#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:12:44 2019

@author: Ignite303
"""

#Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
#
#For example, if s = 'azcbobobegghakl', then your program should print
#
#    Longest substring in alphabetical order is: beggh
#
#In the case of ties, print the first substring. 
#
#For example, if s = 'abcbcd', then your program should print
#
#    Longest substring in alphabetical order is: abc


#SOLUTION 1
#s = 'azcbobobegghakl'
#temp = ''
#
#for i in range(len(s)-1):
#    print s[i:i+1]
#    if i <:
#        
#        
#        if s[0] <= s[1]:
            

#SOLUTION 2

#s = 'azcbobobegghakl'

s = 'abcdefabcdehadhmqrz'

longest = s[0]
current = s[0]
# Both strings are initialized with the first letter

for c in s[1: ]:
# iterate over the input string, starting with the second character
    
    if c >= current[-1]:
        current += c
        
        if len(current) > len(longest):
            longest = current
        
    else:
        current = c
# if c does not fulfill requirement, we start with a new solution current = c
        
print('Longest substring in alphabetical order is: ' + longest)