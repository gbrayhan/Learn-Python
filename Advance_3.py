#Decalracion y conjuntos


print('\n' *100)

conjunto=set('8794')
conjunto2={'3','2','4'}#Conjunto definido
print(conjunto)
print(conjunto2)

#operaciones con conjuntos

print(conjunto & conjunto2)#operacion interseccion
print(conjunto.intersection(conjunto2))#Otra forma


print(conjunto.union(conjunto2))#  no se repiten los elementos en la union
#Diferencia de conjuntos
print(conjunto-conjunto2)
print(conjunto.difference(conjunto2))
#Union exclusiva
print(conjunto ^ conjunto2)
print(conjunto.symmetric_difference(conjunto2))

print("Prueba")

