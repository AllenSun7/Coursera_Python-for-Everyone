#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:05:08 2019

@author: allen
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        break
    print(data.decode())  #decode bytes to unicode
mysock.close()


import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://dr-chuck.com/page1.htm')
for line in fhand:
    print(line.decode().strip())
    
counts = dict()
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
     words = line.decode().split()
     print(line.decode().strip())
     for word in words:   
         counts[word] = counts.get(word, 0) + 1
print(counts)