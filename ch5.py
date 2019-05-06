#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:36:53 2019

@author: allen
"""

largest = None
smallest = None
while True:
    num_type = input("Enter a number: ")
    if num_type == "done" : 
        break
    try:
        num = int(num_type)
    except:
        print("Invalid input")
    if largest == None:
        largest = num
    elif largest < num:
        largest = num
    if smallest == None:
        smallest = num
    elif smallest > num:
        smallest = num
        
print("Maximum is", largest)
print("Minimum is", smallest)