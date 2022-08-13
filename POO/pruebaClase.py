from encapsulamientoGetSet import Persona

print('Creacion objetos'.center(50, '_'))
persona1 = Persona('Sebastian', 'Giron', 33)
persona1.mostrarDetalle()
print(__name__)

print('Eliminación objetos'.center(50, '-'))
del persona1
