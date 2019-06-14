# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:29:34 2019

@author: user
"""

import pandas as pd
from selenium import webdriver

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
    
from collections import OrderedDict

col_name = ["BID NO.","ITEM NO","QUANTITY NO","DEPARTMENT NAME AND ADDRESS","START AND TIME","END DATE AND TIME"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e,f]))
df = pd.DataFrame(col_data) 
df.to_csv("bid_plus.csv",index=False)



    
    

    
    
    
    