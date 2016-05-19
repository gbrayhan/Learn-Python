#Tipos de Datos en Python
entero=2
flotante=18.12
boleano=True
Cadena="Alex"
complejo=1+1j
print (str(entero)+' '+str(flotante))
a=11
b=2
resultado=a//b
print(resultado)

#Potencias en phyton
potencia= a**4
print(potencia)
#nummeros complejos y Operaciones con numeros complejos
numeroComplejo=2+6j
pNumComplejo=numeroComplejo**2
print(pNumComplejo)
#(-32+24j)
raizComplex= numeroComplejo**(1/2)
print(raizComplex)
#Condicionales
edad=18
if edad<18:
    print (Cadena+" es menor de edad")
else:
    print(Cadena+" es mayor de edad")

#Operadores Logicos and, or, not
if not edad<18:
    print (Cadena+" es menor de edad")
else:
    print(Cadena+" es mayor de edad")    
#--Funciones--#
def saludo(nombre):
    print("Hola "+nombre)
   
def sumar(num1=0,num2=0):
    return (num1+num2)
#--Implementacion de Funciones--#
saludo("Alejandro")
print(sumar(2,4))
#--While---#
itsRain=True
while(itsRain==True):
    print("Me pongo sombrilla")
    itsRain=False
print("Seguro que no llueve")

#--Tuplas--#
tupla=("Brayhan Alejandro",12,"044-55-12-22-15-34")
print("El telefono es: "+tupla[2])

tuplaNumeros=(2,32,1,23,344,5,3,2,3)

for numeros in tuplaNumeros:##Siempre empieza desde el inicio
    print(numeros)
##porciones Tupla##
tup1=(12,4,2,33,2,12,3)
tup2=tup1[0:2]##A partir de la 0 quiero 5 elementos

tupla2=tup1[3:]
print(tup1)
print(tupla2)
#Cadenas (String)
nombre="Brayhan Alejandro Gabriel Guerrero"
print(nombre[4:])
#Concatenar Listas
lista1=["Alex",12,1,2]
lista2=["Alexander",112,11,21]
prolist=lista1+lista2
print(prolist)

if 11 in prolist:
    print("Si lo contiene")
else:
    print("No lo contiene")

##Uso negativo de indice 
print(lista1[-1])#Muestra el último elemento de la lista

#--Diccionarios en Phyton--#
diccionario={'Alan':12,"Brenda":23,"Juan":24}

print(diccionario)
print(diccionario["Alan"])
print(len(diccionario),"elementos")

#--Info de funciones aplicadas a tipos de datos--#
tupla=(1,2,3,4,2)
help(tupla)

#--Clases en Phyton--#
class Persona:
    brazos=2
    live=True
    sueno=0
    hambre=0
    sed=0
    cansancio=0
    nombre=""
    def __init__():#Constructor
        self.nombre="Alberto"
        
    def dormir():#Metodos
        sueno=0
        hambre=90
        sed=70
        
    def correr():
        sed=100
        hambre=80
        cansancio=100
        print("Tengo sed y cansancio")

class Hombre(Persona):#Herencia
    pass
    
#Implementacion de clases
Alex= Persona
Brayhan=Hombre
Alex.correr()
Brayhan.correr()
print(Brayhan.sed)

#__Creacion y manejo de archivos__#
def crearArchivo():
    archivo=open("datos.txt",'w')#Modo lectura
    archivo.close()
def escribirArchivo():
    archivo=open("datos.txt",'a')#Modo concatenar a lo que tiene el archivo
    archivo.write("\nAlejandro Gabriel Guerrrero")
    archivo.write("\t5511298877")
    archivo.close()
def leerArchivo():
    archivo=open("datos.txt","r")
    linea=archivo.readline()
    while linea != "":
        print(linea)
        linea=archivo.readline()
    archivo.close()
#__Implementacion de las clases de Archivos__#
    
crearArchivo()
escribirArchivo()
escribirArchivo()
leerArchivo()