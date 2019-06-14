# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:07:57 2019

@author: user
"""

name=input("enter file name")
with open("{}.txt".format(name),mode='rt') as f:
    content=f.readlines()
    print(content[-1])