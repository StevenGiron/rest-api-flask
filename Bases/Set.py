"""
Los set no mantienen un orden, no permiten almacenar elementos duplicados, no se pueden modificar sus elementos pero
 si se pueden eliminar y agregar
"""
# set
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

# Largo
print(len(planetas))

# Revisar si un elemento esta presente
print('Marte' in planetas)

# Agregar elementos
planetas.add('Tierra')
print(planetas)
# No se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

# Eliminar elementos con posible error
planetas.remove('Tierra')
print(planetas)

#Eliminar elemento pero si no existe el elemento no arroja error
planetas.discard('Jupiters')
print(planetas)

# limpiar set
planetas.clear()
print(planetas)


