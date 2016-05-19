import sqlite3
con=sqlite3.connect('python_db.sqlite')#direccion de la base de datos

query="DELETE FROM 'usuarios' WHERE id=1"
con.execute(query)
con.commit()#Todo tipo de cambios
con.close()