

#--Expresiones regulares--#
import re
'''
from xml.dom.minidom import parse,Node
'''
'''para el segundo ejemplo'''
import xml.sax
from xml.etree.ElementTree import parse

patron=re.compile("12\d\d\d")
print(re.search(r"K","kilometro"))#Camel Case
print(re.search(r"\d\d\d\d","kil2233ometro"))
print(patron.search("12332").group())


if(re.search("[Aa][0-9].*(end|fin)$","A2 es una marca y este es el fin")):
    print("se encontró el patrón")

if(re.search("\Aa[0-9].*(end|fin)$","a2 es una marca y este es el fin")):
    print("se encontró el patrón modificando a")

#--Sustitución--#

print(re.sub(r"\d","*","4mangue3ra23"))#Los numeros se reemplazan por caracteres

print(re.sub(r"\d","*","4mangue3ra23",2))#solo los primeros dos se sustituyen

#--modificadores o compiladores--#

expreg=re.compile(r"ab",re.IGNORECASE)
print(expreg.search("Asbisaiabdielabudab"))

#--XML--#
'''Una forma de acceder al codigo xml y a su contenido'''
'''
xmltree=parse("Arch.xml")
for nodo in xmltree.getElementsByTagName("Author"):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType==Node.TEXT_NODE:
            print("El autor del documento xml es: "+nodo_hijo.data)

'''          
'''Otra forma de acceder al codigo xml y a su contenido{REVISAR}'''


xml_doc = parse("Arch.xml")

for ele in xml_doc.findall("Data"):
    print(ele.text)
