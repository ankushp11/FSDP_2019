# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:00:27 2019

@author: user
"""
import requests
url="http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=ultra&apiKey=038faca8fe25432185eb"
response=requests.get(url)
data=response.json()
print("current conversion price:",data['USD_INR'])