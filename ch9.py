#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:34:54 2019

@author: allen
"""

fname = input('Enter file:')
try:
    fhand = open(fname)
except:
    print("Counld fing the file: ", fname)

counts = dict()
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    counts[words[1]] = counts.get(words[1], 0) + 1
    
bigname = None
bigcount = None
for name, count in counts.items():
    if bigname == None or bigcount < count:
        bigcount = count
        bigname = name 

print(bigname, bigcount)