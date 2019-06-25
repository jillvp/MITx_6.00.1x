#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 14:07:12 2019

@author: Ignite303
"""

#x = 25
#epsilon = 0.01
#step = 0.1
#guess = 0.0
#
#while guess <= x:
#    if abs(guess**2 -x) >= epsilon:
#        guess += step
#
#if abs(guess**2 - x) >= epsilon:
#    print('failed')
#else:
#    print('succeeded: ' + str(guess))


x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    
    