# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:06:51 2019

@author: user
"""
import requests

url="http://forsk.in/images/Forsk_logo_bw.png"
response=requests.get(url)

with open("Forsk_logo_bw.png",mode='wb') as f:
    f.write(response.content)