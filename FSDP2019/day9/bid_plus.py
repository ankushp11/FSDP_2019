# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:36:21 2019

@author: user
"""

import pandas as pd
from selenium import webdriver
import mysql.connector
url="https://bidplus.gem.gov.in/bidlists" 

source=webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
source.get(url)

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]

for i in range(1,11):
    a.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    b.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    c.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    d.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    e.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    f.append(source.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)

con=mysql.connector.connect(user='ankushp11', password='ankushp11',
                              host='db4free.net', database = 'ankushp11')
cur=con.cursor()
cur.execute("drop table bid")
cur.execute("create table bid(Bid_no TEXT,item TEXT,quantity INTEGER,dept_name TEXT,start_date TEXT,end_date TEXT)")
for i in range(0,10):
    cur.execute("insert into bid values('{}','{}',{},'{}','{}','{}')".format(a[i],b[i],c[i],d[i],e[i],f[i]))
    con.commit()
     