#--Importar archivos de Json--#
import json
import zipfile
from zipfile import ZipFile
import gzip



import bz2 #bunzip
import tarfile

import smtplib

with open('note.json') as file:
    data=json.load(file)
    
print(data)

print(data['JSON Test Pattern pass3'])

#--Compresion de archivos--#

with zipfile.ZipFile('FotosComprimidas.zip','w') as fzip:
    fzip.write('lacan1.png')
    fzip.write('lacan2.jpg')
    fzip.printdir()
    fzip.extractall()
#--Import gzip--#

with open('lacan1.png','rb') as original:
    with gzip.open("archivo.txt.gz","wb") as archivo1:
        archivo1.writelines(original)
#--Compress bunzip--#


cadena=b"mi cadena mi cadena mi cadena mi cadena mi cadena mi cadena mi cadena mi cadena"
cadena_c=bz2.compress(cadena)

print("Cadena Original" , cadena)
print("Cadena comprimida:\t" , cadena_c)
print("Descomprimir:\t" , bz2.decompress(cadena_c))

#--Compress tarfile--#
archivo_tar=tarfile.open("primer.tar.gz",'w:gz')
archivo_tar.add('lacan2.jpg')
archivo_tar.add('lacan1.png')
archivo_tar.close()
#--Envio de correo--#

from email.mime.text import MIMEText
msg=MIMEText("Este es un correo desde Python")
    

msg['Subject']="Asunto del correo"
msg['From']='gbrayhan@gmail.com'
msg['To']='brayhan_7@hotmail.com'

mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login('gbrayhan@gmail.com','Str1ngth30ry')
mailServer.sendmail('gbrayhan@gmail','gbrayhan@gmail.com',msg_as_string())
mailServer.close()
