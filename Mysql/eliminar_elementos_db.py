import mysql.connector

con=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="db_python")
cursor=con.cursor()

cursor.execute("DELETE FROM `ejemplo` WHERE `id`=1;")
con.commit()#Para que el cambio se realize

cursor.close()
con.close()

