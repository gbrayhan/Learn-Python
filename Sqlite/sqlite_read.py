import sqlite3
con=sqlite3.connect('python_db.sqlite')#direccion de la base de datos


for x in con.execute("SELECT * FROM 'usuarios'"):#rae todo
	print(x)
num=1
for x in con.execute("SELECT * FROM 'usuarios' WHERE id=?",str(num)):
	print(x)

con.close()

