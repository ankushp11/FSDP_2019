# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:35:58 2019

@author: user
"""

with open("romeo.txt",mode='rt') as f:
      file_dict={}
      content=f.readlines()
      print(content)
      for i in content: 
          print(i)
          file=i.split(" ")
          print(file)
          for j in file:
              for k in content: 
                 file1=k.split(" ")
              print(file1)
              file_dict[j]=file1.count(j)
      print(file_dict)