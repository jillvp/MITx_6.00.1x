#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 05:19:58 2019

@author: Ignite303
"""

s = 'abcbobobdebobfg'

numBob = 0

for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        numBob +=1
        
print ("Number of times bob occurs is: " + str(numBob))
