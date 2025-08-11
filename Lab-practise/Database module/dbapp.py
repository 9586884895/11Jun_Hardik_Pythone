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

#update data
"""update_data="update studinfo set name='harsh',city='baroda' where id=2"
try:
    db.execute(update_data)
    db.commit()
    print("Record Updated")
except Exception as e:
    print(e)"""

#delete data
"""Delete_data="delete from studinfo where id=3"
try:
    db.execute(Delete_data)
    db.commit()
    print("Record Deleted")
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
        print(i[0])
except Exception as e:
    print(e)

