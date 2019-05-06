#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:37:44 2019

@author: allen
"""

import xml.etree.ElementTree as ET
 
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))