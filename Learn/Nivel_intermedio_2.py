from functools import reduce

#--Hilos--#
'''
import threading
import time

class miHilo(threading.Thread):
    def run(self):
        print("{} Inicio".format(self.getName()))
        time.sleep(1)
        print("{} Terminado".format(self.getName()))


if __name__=="__main__":
    for x in range(3):
        hilo=miHilo(name="Hilo-{}".format(x+1))
        hilo.start()
        time.sleep(0.1)
'''
#--Iteracion--#
lista=[1,23,4,5,3,4]

for elemento in lista:
    print(elemento)

for linea in open("lugares.txt"):#Iteracion en texto
    print(linea)

#--Generador--#

def numeros():
    n=1
    while True:
        yield n
        n=n+1

i=numeros()

print(i)
print(i.__next__())
print(i.__next__())
#Otro ejemple de generadores
'''
#Definimos nuestra funcion
def pares():
    index=1
    #En este caso definimos un bucle infininto
    while True:
        yield index*2
        index+=1

if __name__ == '__main__':
    for i in pares():
        print(i)
'''  
#Ejemplo 3 de generadores
'''
def multiplos(n):
    ini=1
    while True:
        yield ini*n
        ini+=1
if __name__ == '__main__':
    for j in multiplos(3):
        print(j)
'''
#--Closures en phyton--#
def functionA(x):
    def functionB(y):
        return x*y
    return functionB

miFuncion=functionA(3)#Primer parametro "x"
print(miFuncion(1))#Segundo parametro "y"

#--Decorador--#

def primerD(funciona):
    def funciondecorada(*argumentos,**kwars):
        print("Primer decorador")
    return funciondecorada
        
@primerD#antes de la funcion que se quiere decorar  
def funciona():
    print("Mi primer decorador")#con el decorador éste ya no es el resultado
    
funciona()


#Programacion funcional

def lower(elementos):return elementos.lower()
miLista=["Jose","JUAN","pedro"]
print(list(map(lower,miLista)))
#map filter reduce programacion funcional
print([cad.lower() for cad in miLista])#Manera tradicional

#Funciones de orden superior#
def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("Hi")
    idioma_func={"es":saludo_es,
                 "en":saludo_en
                 }
    return idioma_func[idioma]

saludame=saludo("en")
saludame()
#Otro ejemplo de programacion funcional se importa reduce

numeros=(2,3,4,2)
def suma(x,y):
    return x+y
sumar=reduce(suma,numeros)#reduce pertenece a functools
print(sumar)


        
        


















