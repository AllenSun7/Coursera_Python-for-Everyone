#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 23:20:45 2019

@author: allen
"""

# get the target url
import urllib.request as urlrequest
from bs4 import BeautifulSoup

actual_data_url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
page = urlrequest.urlopen(actual_data_url)
soup = BeautifulSoup(page, 'html.parser')

#get info
counts = dict()
tags = soup('a')    
print(tags[6].get_text())
for tag in tags:    
    counts[tag.get_text()] = counts.get(tag.get_text(), 0) + 1
print(counts)