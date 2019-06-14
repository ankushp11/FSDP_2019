# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 17:43:12 2019

@author: user
"""

from bs4 import BeautifulSoup as BS
import requests
import sqlite3
import pandas as pd  
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
        
con=sqlite3.connect('cricket.db')
cur=con.cursor()

cur.execute("CREATE TABLE rank(position INTEGER,team_name TEXT,rating INTEGER)")

for i in range(0,16):
     cur.execute("INSERT INTO rank VALUES({},'{}',{})".format(a[i],b[i],c[i]))

con.commit()     
cur.execute("Select * from rank")

df=pd.DataFrame(cur.fetchall())
df.columns=["POSITION","TEAM NAME","RATING"]
con.commit()
con.close()