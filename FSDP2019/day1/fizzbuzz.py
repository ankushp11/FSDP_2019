# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:46:36 2019

@author: user
"""
for i in range(1,101):
    if(i%3==0 and i%5==0):
        print("fizzbuzz")
    elif(i%3==0):
        print("fizz")
    elif(i%5==0):
        print("buzz")
    else:
        print(i)