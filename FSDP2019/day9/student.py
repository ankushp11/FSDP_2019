# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:31:41 2019

@author: user
"""

import sqlite3
import pandas as pd
con=sqlite3.connect('university2.db')

cur=con.cursor()

cur.execute("""CREATE TABLE student(
               student_name TEXT,
               student_Age INTEGER ,
               student_roll_no INTEGER,
               student_Branch TEXT)""")


cur.execute("INSERT INTO student VALUES('ankush',19,24,'cse')")
cur.execute("INSERT INTO student VALUES('ashutosh',20,25,'cse')")
cur.execute("INSERT INTO student VALUES('aayush',19,26,'cse')")
cur.execute("INSERT INTO student VALUES('himanshu',20,27,'cse')")
cur.execute("INSERT INTO student VALUES('hemant',20,28,'cse')")
cur.execute("INSERT INTO student VALUES('garvit',19,29,'cse')")
cur.execute("INSERT INTO student VALUES('divyansh',19,30,'cse')")
cur.execute("INSERT INTO student VALUES('deepak',19,31,'cse')")
cur.execute("INSERT INTO student VALUES('ankit',19,32,'cse')")
cur.execute("INSERT INTO student VALUES('dilip',20,33,'cse')")
cur.execute("SELECT * from student")
con.commit()


df =pd.DataFrame(cur.fetchall())  
df.columns = ["student_name","student_age","student_roll_no","student_branch"]
con.commit()
con.close()
