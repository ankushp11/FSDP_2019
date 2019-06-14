# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:24:53 2019

@author: Amisha Garg
"""

def fix_teen(n):
    s=0
    a=n.values()
    for item in a:
        if item>=13 and item<=19 and item!=15 and item!=16:
            item=0
        s=s+item
    print(s)
dic=  {"a" : 2, "b" : 15, "c" : 13}
fix_teen(dic)
        