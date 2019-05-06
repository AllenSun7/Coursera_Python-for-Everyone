#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:36:37 2019

@author: allen
"""

counts = dict()
cpos = 0
fhand = open ('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) < 6 or words[0] != 'From':
        continue
    cpos = words[5].find(':')
    counts[words[5][:2]] = counts.get(words[5][:cpos], 0) + 1
tmp = list()
for key, val in sorted(counts.items()):
    newt = (key, val)
    tmp.append(newt)
print(tmp) 