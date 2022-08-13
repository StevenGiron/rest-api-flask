# Listas
nombres = ['Steven', 'Sebastian', 'Juan', 'Pipe']
print(nombres[0], nombres[1], nombres[2])

# Acceder de manera inversa
print(nombres[-1], nombres[-2], nombres[-3], )

# imprimir un rango
print(nombres[0:3])

# Del inicio hasta el indice sin incluirlo
print(nombres[:2])

# Desde el indice indicado hasta el final
print(nombres[2:])

# Iterar una lista
for nombre in nombres:
    print(nombre)

# Largo de una lista
print(len(nombres))

# Agregar nuevo elemento a la lista
nombres.append('Ricardo')
print(nombres)

# Insertar elemento en un indice especifico
nombres.insert(1, 'Alejandra')
print(nombres)

# Eliminar elemento
nombres.remove('Ricardo')
print(nombres)

# Eliminar el ultimo valor agregado
nombres.pop()
print(nombres)

# Eliminar un indice
del nombres[0]
print(nombres)

# Limpiar la lista
nombres.clear()
print(nombres)

# Borrar la lista por completo
del nombres
print(nombres)
