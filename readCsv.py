import csv

doc=open('Prueba.csv','r')#Modo de lectura sin modificar
doc_csv=csv.reader(doc)

for (nombre,numero) in doc_csv:
    print nombre,numero

doc.close()

