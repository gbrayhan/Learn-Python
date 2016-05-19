import mysql.connector

con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="db_python")
cursor=con.cursor()

#cursor.execute("CREATE TABLE ejemplo(id INT,data VARCHAR(20));")#Crear tabla
for x in xrange(1,10):
	cursor.execute("INSERT INTO ejemplo (id,data) VALUES ("+str(x)+",'Mis datos 2')")#Insertar datos en la tabla

cursor.execute("SELECT * FROM `ejemplo` WHERE `id`=12")


rows=cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
con.commit()#Necesario para insertar
con.close()


