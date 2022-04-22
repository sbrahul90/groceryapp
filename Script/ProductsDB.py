import sqlite3

cn = sqlite3.connect("Product.DB")
print('database created')

tab = cn.execute('''create table _product (id int not null,category char not null,pname char not null,brand varchar not null,quantity varchar not null,price varchar not null)''')
print(tab)
print('table opened to insert data')


"""cn.execute("update _product set price=15  where id=35")
cn.commit()"""

"""cn.execute("delete from _product where id=11")
cn.commit() """

cn.execute('''CREATE TABLE _Cart
            (Name char,
             id INTEGER,
             Email varchar,
             FOREIGN KEY(Name) REFERENCES users(Name),
             FOREIGN KEY(id) REFERENCES _product(id),
             FOREIGN KEY(Email) REFERENCES users(Email))''')

print("successful")