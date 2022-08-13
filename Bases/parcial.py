# definicion de la variable auxiliar
def porcentaje_actividad(a, b, c, d):
    print(f'El porcentaje de personas que lee es de: {a / (a + b + c) * 100}')
    print(f'El porcentaje de personas que ve television es de: {b / (a + b + c) * 100}')
    print(f'El porcentaje de personas que ve hace deporte es de: {c / (a + b + c) * 100}')
    print(f'El porcentaje de personas que duerme es de: {d / (a + b + c) * 100}')


# lectura de datos y declaracion de variables
n = int(input('digitel el numero de personas: '))
i = 0
leer = 0
ver_television = 0
hacer_deporte = 0
dormir = 0
leer_y_6_9 = 0
ver_tv_9 = 0

# programa rpincipal
while i < n:
    i += 1
    tiempo_libre = int(input(f'para la persona {i} digite el tiempo libre en horas: '))
    actividad = int(input(f'para la persona {i} digite la actividad siendo 1: leer 2: ver television 3: hacer deporte 4: dormir: '))
    if actividad == 1:
        leer += 1
    elif actividad == 2:
        ver_television += 1
    elif actividad == 3:
        hacer_deporte += 1
    elif actividad == 4:
        dormir += 1
    if 6 <= tiempo_libre <= 9 and actividad == 1:
        leer_y_6_9 += 1
    if tiempo_libre > 9 and actividad == 2:
        ver_tv_9 += 1



print(porcentaje_actividad(leer, ver_television, hacer_deporte, dormir))
print(f'el porcentaje de personas que tiene entre 6 y 9 horas libres y prefieren leer es de: {(leer_y_6_9/n) * 100}')
print(f'El numero de personas que prefiere ver television y tiene mas de 9 horas libres es: {ver_tv_9}')
