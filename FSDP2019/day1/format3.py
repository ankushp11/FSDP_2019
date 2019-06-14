# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:39:13 2019

@author: user
"""

str=input("enter a string:")
pos=str.__len__()
print(str[0]+str[1:pos-1].replace("","*")+str[pos-1])