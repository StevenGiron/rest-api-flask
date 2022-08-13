# diccionario (key, Value) al igual que el set no existen indices en un diccionario
diccionario = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

# Conocer el largo
print(len(diccionario))

# Acceder a un elemento, Se indica la llave
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)

# Recorrer los elementos - sus llaves
for termino in diccionario:
    print(termino)

# Recorrer los elementos - sus llaves y valores
for key, value in diccionario.items():
    print(key, value)

print('')

# Recuperar solo los valores
for value in diccionario.values():
    print(value)

# Comprobar existencia de algun elemento
print('IDE' in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar elemento
diccionario.pop('DBMS')
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario
print(diccionario)
