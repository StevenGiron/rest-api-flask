"""
Una tupla a difetencia de una lista, sus elementos no pueden
ser modificados ni eliminados ni agregar nuevos elementos (inmutable)
"""

# Definir una tupla
frutas = ('Naranja', 'Platano', 'Guayaba', 'Manzana')
print(frutas)

# Largo de una tubla
print(len(frutas))

# Acceder a un elemento
print(frutas[0])

# Rango
print(frutas[0: 3])

for fruta in frutas:
    print(fruta, end=' ')

# Converitr tupla a lista
frutas_lista = list(frutas)
# se modifica la lista
frutas_lista[0] = 'Pera'
# Se convierte nuevamente a una lista
frutas = tuple(frutas_lista)
print('\n', frutas)

# eliminar tupla
del frutas
print(frutas)


