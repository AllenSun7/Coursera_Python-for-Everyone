#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:38:45 2019

@author: lun sun
"""


    

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0.0
s_confidence = 0.0
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
    
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        sppos = line.find(" ")
        count = count + 1
        value = float(line[sppos+1: ])
        s_confidence = s_confidence + value
        
print("Average spam confidence:", s_confidence / count)
