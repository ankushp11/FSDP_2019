# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:06:24 2019

@author: user
"""
li=input().split(",")
l1=[ int(i)>0 for i in [i[::-1]==i for i in li]  ]
print(all(l1))
        