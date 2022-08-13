from cuadradoHerenciaMultiple import Cuadrado

cuadrado1 = Cuadrado(4, 'Rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcularArea())

# MRO Method Resolution Order
print(Cuadrado.mro())

