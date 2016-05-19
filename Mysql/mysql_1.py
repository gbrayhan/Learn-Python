import mysql.connector

con = mysql.connector.connect(user="root", password="",host="127.0.0.1",port=8080,database="dbpython")

cursor=con.cursor()
cursor.execute("CREATE TABLE example (id INT,data VARCHAR(100));")
con.close()
