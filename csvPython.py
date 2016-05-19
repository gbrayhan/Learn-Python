import csv

archivoCsv=open('MiArchivo.csv','w')#Modo escritura

doc_csv_w=csv.writer(archivoCsv)

lista=[["Pedro",2322],["Brayhan",23],["Elizabeth",211]]

#doc_csv_w.writerows(lista)#Manda un interlineado de una fila#


'''Mejor manejo de datos, agregando algun if'''
for x in lista:
    doc_csv_w.writerow(x)

archivoCsv.close()
