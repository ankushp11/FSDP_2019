# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:29:29 2019

@author: user
"""

import requests

url= "http://api.openweathermap.org/data/2.5/weather?q=Udaipur&appid=e9185b28e9969fb7a300801eb026de9c"
response=requests.get(url)
my_data=response.json()
print("longitude:",my_data['coord']['lon'])
print("latitude:",my_data['coord']['lat'])
print("weather_cond:",my_data['weather'][0]['main'])
print("wind speed:",my_data['wind']['speed'])
print("sunrise time:",my_data['sys']['sunrise'])
print("sunset time:",my_data['sys']['sunset'])