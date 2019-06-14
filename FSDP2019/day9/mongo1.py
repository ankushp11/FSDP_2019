# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:28:21 2019

@author: user
"""

import pymongo



client = pymongo.MongoClient("mongodb+srv://ankush_31:ankushp@cluster0-sfhhi.mongodb.net/test?retryWrites=true&w=majority")



db = client.test

def add_details(name,age,roll,branch):
    unique_student = db.student.find_one({"student_roll_no":roll})
    if unique_student:
        return "student already exists"
    else:
        db.student.insert(
                {
                "student_name" : name,
                "student_age" : age,
                "student_roll_no" : roll,
                "student_branch" : branch
                })
        return "student added successfully"
add_details('ankush',19,24,'cse')
add_details('ashutosh',20,25,'cse')
add_details('aayush',20,26,'cse')
add_details('himanshu',20,26,'cse')
add_details('hemant',20,27,'cse')
add_details('garvit',19,28,'cse')
add_details('divyansh',19,29,'cse')
add_details('dilip',19,30,'cse')
add_details('deepak',19,31,'cse')
add_details('ankit',19,23,'cse')

def fetch_all_student():
    user = db.student.find()
    for i in user:
        print (i)

fetch_all_student()

