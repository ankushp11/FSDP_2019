# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:49:57 2019

@author: user
"""
with open("words.txt",mode='rt') as f:
     with  open("words1.txt",mode='wt') as f1:
        for line in f:
            f1.write(line)