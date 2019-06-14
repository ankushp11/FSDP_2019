# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:24:55 2019

@author: user
"""
import re
l=[]
str=input("enter a email addresses").split(",")
for i in str:
    res=re.findall('[a-z0-9_-]+@[\w]+\.[a-z]{2,4}$',i)
    for j in res:
        l.append(j)
        l.sort()
print(l)        
        