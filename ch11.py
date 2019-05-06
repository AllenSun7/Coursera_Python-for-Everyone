#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:19:57 2019

@author: allen
"""

import re
snum = 0
fhand = open('actualdata.txt')
for lines in fhand:
    line = re.findall('[0-9]+', lines)
    if len(line) == 0:
        continue
    for num in line:
        snum = snum + int(num)
print('sum of the numbers: ', snum)