#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 22:59:37 2019

@author: allen
"""

# get the target url
import urllib.request as urlrequest
from bs4 import BeautifulSoup

actualdata_url = 'http://py4e-data.dr-chuck.net/comments_226005.html'
page = urlrequest.urlopen(actualdata_url)
soup = BeautifulSoup(page, 'html.parser')

#get info
snum = 0
tags = soup('span')
for tag in tags:
    num = int(tag.get_text())
    snum = snum + num
print(snum)