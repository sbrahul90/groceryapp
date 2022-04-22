import sqlite3

cn = sqlite3.connect("customerdata.DB")
print("Database opened successfully")

#cn.execute('''create table users (Name char not null, Address varchar NOT NULL, Age int not null, Contact varchar NOT NULL, Email varchar NOT NULL, password varchar NOT NULL,cpassword varchar NOT NULL,gender char NOT NULL)''')

#print("Table created successfully")

"""tab = cn.execute('''create table _product_ (id int not null,category char not null,pname char not null,brand varchar not null,quantity int not null,price int not null)''')

print(tab)
print('table opened to insert data')


cn.execute('''CREATE TABLE addcart
            (pdName varchar,
             price int,
             quantity int)''')

cn.execute('''CREATE TABLE ordercart
            (pdName varchar,
             quantity int,
             price int)''')

print("success")"""

cn.execute('''CREATE TABLE vieworder
            (cName varchar,
             pdName varchar,
             quantity int,
             price int)''')


"""cn.execute("delete from _product_ where id=3")
cn.commit() """


"""cn.execute("delete from addcart where quantity='1' ")
cn.commit()


dta = cn.execute("select * from addcart")
for i in dta:
    print(i)"""