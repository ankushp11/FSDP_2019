# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:05:57 2019

@author: user
"""
with open("absentee.txt",mode='wt') as f:
    x=1
    while x<=25:
        name=input("enter a name")
        if (not name):
            break
        else:
            x=x+1
            f.write(name+"\n")
f1=open("absentee.txt",mode='rt')        
file_content=f1.readlines()
for i in file_content:
    print(i)
    
f1.close()    