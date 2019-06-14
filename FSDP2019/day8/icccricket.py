# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:47:42 2019

@author: user
"""

from bs4 import BeautifulSoup as BS
import requests

url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"

source=requests.get(url).text

soup=BS(source,"lxml")
ptable=soup.find('table',class_='table')
#print(ptable.prettify())
a=[]
b=[]
c=[]
for i in ptable.findAll('tr'):
    cell=i.findAll('td')
    if len(cell)==5:
        a.append(cell[0].text.strip())
        b.append(cell[1].text.strip())
        c.append(cell[4].text.strip())
        
from collections import OrderedDict
c_name=["RANK","TEAM NAME","POINTS"]        
c_data=OrderedDict(zip(c_name,[a,b,c]))


import pandas as pd
df=pd.DataFrame(c_data)
df.to_csv("ranking.csv",index=False)       

        
