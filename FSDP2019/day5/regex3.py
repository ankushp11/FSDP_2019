# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:49:05 2019

@author: user
"""
import re
str=input("enter card number")
res=re.findall('^[456][\d]{3}[^,_]-[\d]{4}[^,_]-[\d]{4}[^,_]-[\d]{4}[^,_]',str)
print(res)