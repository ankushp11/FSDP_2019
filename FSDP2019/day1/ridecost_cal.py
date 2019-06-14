# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:34:51 2019

@author: user
"""
km=int(input("enter total kilometer travelled"))
disel_price=80
avg_of_vehicle=18
fuel_used=(km/avg_of_vehicle)
total_cost=(disel_price*fuel_used)
print("total cost of riding:",round(total_cost),"INR")