# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:51:12 2019

@author: user
"""
c=0
for j in range(0,7):
   if(c==0):
      for i in range(0,16):
         if(i%2==0):
           print("*",end=" ")
      print("\n")  
      c=1    
   else:
       for j in range(0,16):
           if(j%2!=0):
               print("*",end="")
           else:
               print(" ",end="")
       print("\n")
       c=0