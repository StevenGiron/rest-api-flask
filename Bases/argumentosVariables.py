def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)


listarNombres('Steven', 'Sebastian', 'Juan')
listarNombres('Dahiana', 'Aleja')


# Argumentos variables llave-valor
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(llave, valor)


listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
