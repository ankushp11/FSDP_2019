# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:45:09 2019

@author: user
"""

a1=round(float(input("enter marks of assignment 1:")))
a2=round(float(input("enter marks of assignment 2:")))
a3=round(float(input("enter marks of assignment 3:")))
e1=round(float(input("enter marks of exam 1:")))
e2=round(float(input("enter marks of exam 2:")))
weighted_score=((a1+a2+a3)*0.1)+(e1+e2)*0.35
print("total weighted score:",weighted_score)