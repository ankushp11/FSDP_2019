# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:04:56 2019

@author: user
"""

names = ['Mary', 'Isla', 'Sam']
l1=list(map(lambda i:hash(i),names))
print(l1)