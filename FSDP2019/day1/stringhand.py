# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:19:44 2019

@author: user
"""

name=input("enter your full name:")
pos=name.index(" ")
new_name=name[pos+1:]+" "+name[:pos]
print(new_name)
