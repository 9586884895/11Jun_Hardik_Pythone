import pymysql

try:
    db=pymysql.connect(host='localhost',user='root',password='',database='morningdb')
    print("Database connected")
except Exception as e:
    print(e)

cr=db.cursor() # table creation process
"""tbl_create="create table studinfo(id integer primary key auto_increment,name text,city text)"

try:
    cr.execute(tbl_create)
    print("Table created sucessfully")
except Exception as e:
    print(e)"""

"""insert_data="insert into studinfo(name,city)values('Hardik','Ahmedabad'),('jayesh','Rajkot'),('Ramesh','Piplana'),('Paresh','Jodhpur'),('Pratham','Delhi')"
try:
    cr.execute(insert_data)
    db.commit()
    print("Record Inserted")
except Exception as e:
    print(e)"""

"""update_data="update studinfo set name='harsh',city='baroda' where id=2"
try:
    cr.execute(update_data)
    db.commit()
    print("Record Updated")
except Exception as e:
    print(e)"""

"""Delete_data="delete from studinfo where id=3"
try:
    cr.execute(Delete_data)
    db.commit()
    print("Record Deleted")
except Exception as e:
    print(e)"""

cr=db.cursor()
show_data="select *from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i[1])
except Exception as e:
    print(e)