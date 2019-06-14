# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 00:20:31 2019

@author: user
"""
str=input("enter a string")
r1=input("enter a alphabet to be replaced")
r2=input("enter a alphabet for repacement")
pos=str.find(r1)
new_str=str[:pos+1]+str[pos+1:].replace(r1,r2)
print(new_str)