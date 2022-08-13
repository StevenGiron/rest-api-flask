# Crear clase metodo __init__
class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


# Crear objeto de la clase (instancia)
persona1 = Persona('Steven', 'Girón', 23)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')
persona1.mostrarDetalle()

# Llamar metodo desde la clase
Persona.mostrarDetalle(persona1) # No es muy comun

# Agregar nuevo atributo desde el objeto
persona1.telefono = '318435786'
print(persona1.telefono)
