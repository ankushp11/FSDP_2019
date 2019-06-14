# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:23:25 2019

@author: user
"""

import json
import requests
Host="https://enm5pgpco8dj.x.pipedream.net/"
data = {"firstname":"dev","language":"English"}
headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}
def post_method():
    response = requests.post(Host,data,headers)
    return response
print ( post_method().text )
