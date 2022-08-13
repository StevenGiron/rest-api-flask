class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea (self):
        return  self.base * self.altura


b = float(input('Digite la base del rectangulo: '))
h = float(input('Digite la altura del rectangulo: '))
rectangulo1 = Rectangulo(b, h)
print(f'El area del rectangulo es: {rectangulo1.calcularArea()}')