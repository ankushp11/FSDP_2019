# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:56:16 2019

@author: user
"""

import random
names = ['Mary', 'Isla', 'Sam']
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']
name=list(map(lambda i:random.choice(code_names) ,names))
print(name)