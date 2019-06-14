# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:34:54 2019

@author: user
"""

with open("romeo.txt",mode='rt') as f:
    content=f.readlines()
    l=[]
    c=0
    c1=0
    pos=f.tell()
    print(pos)
    f.seek(0,0)
    for i in content:
        c1=c1+1
        l.append(i.split(" "))    
    for j in l:
        for k in j:
            c=c+1
            
    print(c)   
    print(c1)
    