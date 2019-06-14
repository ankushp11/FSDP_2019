# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:02:20 2019

@author: user
"""
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
l1=[]
for i in orders:
     y=i[2]*i[3]
     if(y<100.0):
         t=(i[0],y+10)
         l1.append(t)    
     else:
         t=(i[0],y)
         l1.append(t)
print(l1)        
     

######################################################



orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]]
lt=[]
l1=map(lambda x : x[0],orders)
l2=map(lambda x:(x[2]*x[3])+10 if x[2]*x[3]<100.0 else x[2]*x[3],orders)
l3=list(zip(l1,l2))
print(l3)