#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:02:38 2019

@author: allen
"""
# Get the name of the dile and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
#    print(words)    
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
# Find the most common word
bigcount = None
bidword = None
for word, count in counts.items():
    if bigcount is None or count >bigcount:
        bigword = word
        bigcount = count

# All done
print("bigword", "bigcount")
print(bigword, bigcount)
handle.close()

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
bigcount = None
bigword = None
for word, count in counts.items():
    if bigword == None or bigcount < count:
        bigcount = count
        bigword = word 

print('bigword', 'bigcount')
print(bigword, bigcount)