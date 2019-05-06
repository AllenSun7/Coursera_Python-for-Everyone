#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:30:28 2019

@author: allen
"""



fhand = open("mbox-short.txt")
count = 0
for line in fhand:   
    line = line.rstrip()
    words = line.split()
    if len(words) < 1 or words[0] != "From":
        continue
    print(words[1])
    count = count + 1 
print("There were", count, "lines in the file with From as the first word")
