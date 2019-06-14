# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:09:57 2019

@author: user
"""

from functools import reduce
people = [{'name': 'Mary', 'height': 160},{'name': 'Isla', 'height': 80},{'name': 'Sam'}]

          
l1=reduce(lambda w,z :w+z ,map(lambda y :y['height'],filter(lambda x :'height' in x , people)))
height_count=len(list(filter(lambda x :'height' in x , people)))
average_height=l1/height_count
print(average_height)