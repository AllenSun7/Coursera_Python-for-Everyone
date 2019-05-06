#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 19:37:52 2019

@author: allen
"""
getNumbers = 0
while getNumbers == 0: 
    score = input("Enter Score: ")
    try:        
        s = float(score)
        getNumbers = 1
    except:
        print("Error, please enter numeric input")
if s > 1.0 or s < 0.0:
    print("Error")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.7:
    print("F")