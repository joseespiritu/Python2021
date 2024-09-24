# Dar formato a un str
nombre = 'Jose'
edad = 28
sueldo = 3000

### Fstring literal
mensaje=f'Nombre {nombre} Edad {edad} Sueldo {sueldo:.2f}'
print(mensaje)

#Método print
print(nombre, edad, sueldo, sep=', ')

### FORMAT
# mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#
# mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
# mensaje = 'Sueldo {2:.2f} Nombre {0} Edad {1}'.format(nombre, edad, sueldo)
#
# mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'.format(n=nombre, s=sueldo, e=edad)
#
# diccionario = {'nombre': 'Ivan', 'edad':35, 'sueldo':8000.00}
# mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
# print(mensaje)

##### PARAMETROS
# mensaje_con_formato = 'Mi nombre es %s y tengo %d años'%(nombre,edad)
#
# persona = ('Karla', 'Gomez', 5000.00)
# # mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
# # print(mensaje_con_formato)
# mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'
# print(mensaje_con_formato%persona)
