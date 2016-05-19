#Python Intermedio

#Variables de instancia y de Clase
class Persona():
        edad=18#Variable de Clase
        def __init__(self,nombre,nacionalidad):
                self.nombre=nombre #Variable de instancia
                self.nacionalidad=nacionalidad
        def nadar(self):#Metodo de instancia se recibe el self
                print("Estoy nadando")
                
per1=Persona("José","Mexicano")
per1.nadar()

#--Metodo de clase--#
class Movil():
        def __init__(self):
                pass
        
        def despedir(self):#Metodo de instancia
                print("Adios")

        @classmethod
        def saludar(cls,nombre):##Metodo de clase
                print("Hola "+nombre)

#Sin necesidad de crear un objeto se usa el metodo de la clase
Movil.saludar("Alejandro")  


#--Metodo Estatico--#
class Animal():
        def __init__(self):
                pass
        def brincar(self):
                print("Brinco")
        @classmethod
        def corer(cls):
                print("Corro")
        @staticmethod#Metodo estatico no se necesita ningun argumento
        def nadar():
                print("Nado")

#--Metodos Especiales--#
class Clase():
        def __new__(cls):
                print("New")
                return super().__new__(cls)#super regresa la instancia
        def __init__(self):
                print("Init")
#--Propiedades de los objetos--#
class Circulo():
        def __init__(self,radio):
                self.radio=radio
        @property
        def area(self):
                return (3.1416*(self.radio**2))

#--Polimorfismo--#

class Perro():
        def avanzar(self):
                print("4 Patas")
class Perico():
        def avanzar(self):
                print("volar")

def mover(animal):
        animal.avanzar()
#--Introspeccion--#        
class Intro():
        verdato=9
        def __init__(self,valor):
                self.valor=valor
        def segundo(self):
                print("Segundo")
        def tercero(self):
                print("Tercero")
        

perro=Animal()
perro.nadar()#Estatico
c=Clase()#Metodos especiales

c=Circulo(10)
print(c.area)#Propiedades

dog=Perro()
perico=Perico()

perico.avanzar()
dog.avanzar()
print("Con polimorfismo")
mover(perico)
mover(dog)
#Introspeccion
##dir,isinstance,hasattr
dato=Intro("valor")
print(dir(dato))
print(isinstance(dato,Intro))##Si pertencece a la clase
print(hasattr(dato,"verdato"))##Si existe el atributo

#--Excepciones--#
lista=[2,3]
try:
        print(lista[5])
except IndexError:
        print("Error en el indice")
else:
        print("No hay errror")
finally:
        print("Se ejecuto")
#--Lanzar excepciones--#
try:
        raise TypeError
except:
        print("Errores con los tipos")

#--Excepciones definidas--#

class Err(Exception):
        def __init__(self, valor):
                print("el error por valor",valor)
try:
        raise Err(4)
except Err:
        print("Error Escrito")

