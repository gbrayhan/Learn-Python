#Para crear la tabla

#CREATE TABLE "usuarios" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT NOT  NULL, "nombre" TEXT, "tipo" TEXT,"edad" INTEGER)
import sqlite3
con=sqlite3.connect('python_db.sqlite')

query="INSERT INTO 'usuarios' ('nombre','tipo','edad') VALUES ('Alejandra','normal','13')"


con.execute(query)

con.commit()
con.close()