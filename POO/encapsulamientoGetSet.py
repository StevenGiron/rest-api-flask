class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrarDetalle(self):
        print(f'{self._nombre} {self._apellido} {self._edad}')

    def __del__(self):
        print(f'Persona eliminada: {self._nombre} {self._apellido}')


if __name__ == '__main__':
    persona1 = Persona('Steven', 'Giron', str(23))
    print(persona1.nombre)

    persona1.nombre = 'Carlos'
    print(persona1.nombre)

    persona1.mostrarDetalle()

    print(__name__)
