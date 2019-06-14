# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:31:49 2019

@author: user
"""
import re
str=input("enter a number").split(",")
for i in str:
    res=re.findall('[+-]*[0-9]*\.[0-9]+',i)
if(res):
     print("True")
else:
     print("False")