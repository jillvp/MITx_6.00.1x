#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 03:58:09 2019

@author: Ignite303
"""

string = "qwertyyuiopsaskdmnxi"
numVowels = 0

for char in string:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
        
print('Number of vowels: ' + str(numVowels))


numBob = 0

