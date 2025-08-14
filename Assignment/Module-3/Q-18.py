#18.Write a Python program to create a database and a table using SQLite3.
#19.Write a Python program to insert data into an SQLite3 database and fetch it.

import sqlite3

try:
    db=sqlite3.connect("temp.db")
    print("database created/connected sucessfully")
except Exception as e:
    print(e)

#table create
Tbl_create="create table studinfo(id integer primary key autoincrement,name text,city text)"

try:
    db.execute(Tbl_create)
    print("table Created")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('Hardik','Ahmedabad'),('jayesh','Rajkot'),('Ramesh','Piplana'),('Paresh','Jodhpur'),('Pratham','Delhi')"
try:
    db.execute(insert_data)
    db.commit()
    print("Record Inserted")
except Exception as e:
    print(e)"""

# Showdata
cr=db.cursor()
show_data="select *from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i)
except Exception as e:
    print(e)