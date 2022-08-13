class Aritmetica:
    """
    Clase para realizar las operaciones de suma, resta, etc.
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def Sumar(self):
        return self.operandoA + self.operandoB

    def Restar(self):
        return self.operandoA - self.operandoB


aritmetica1 = Aritmetica(5, 2)
print(f'Suma: {aritmetica1.Sumar()}'
      f'\nResta: {aritmetica1.Restar()}')




