# Profundizando en el tipo str

#### SEPARAR VALORES
# help(str.split)
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
# print(f'lista cursos: {lista_cursos}')
# print(type(lista_cursos))

cursos_separados_coma = 'Java, Python, JavaScript, Angular, Spring, Excel'
lista_cursos = cursos_separados_coma.split(', ')
# print(f'lista cursos: {lista_cursos}')
# print(len(lista_cursos))

lista_cursos = cursos_separados_coma.split(', ', 3)
print(f'lista cursos: {lista_cursos}')
print(len(lista_cursos))

###### UNIR VALORES
# help(str.join)
# tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
# mensaje = ' '.join(tupla_str)
# print(f'mensaje: {mensaje}')
#
# lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
# mensaje = ', '.join(lista_cursos)
# print(f'mensaje: {mensaje}')
#
# cadena = 'HolaMundo'
# mensaje = '.'.join(cadena)
# print(f'mensaje: {mensaje}')
#
# diccionario = {'nombre': 'José', 'apellido': 'Espíritu', 'edad': '18'}
# llaves = ' '.join(diccionario.keys())
# valores = ' '.join(diccionario.values())
# print(f'llaves: {llaves}, type: {type(llaves)}')
# print(f'valores: {valores}, type: {type(valores)}')

### INMUTABILIDAD
# help(str.capitalize)
# mensaje1 = 'hola mundo'
# mensaje2 = mensaje1.capitalize()
# print(f'mensaje1: {mensaje1}, id{hex(id(mensaje1))}')
# print(f'mensaje2: {mensaje2}, id{hex(id(mensaje2))}')
#
# mensaje1 += 'adios'
# print(f'mensaje1: {mensaje1}, id{hex(id(mensaje1))}')

# Concatenación automática en python
# variable = 'Adios'
# mensaje = 'Hola' 'Mundo' + variable
# mensaje += 'Universidad' 'Python'
# print(mensaje)

# import math
# help(math.isnan)
# help(str.capitalize)
#
# from mi_clase import MiClase
# help(MiClase)
#
# # Solo la definición
# print(MiClase.__doc__)
#
# # Documentación del método init
# print(MiClase.__init__.__doc__)
#
# # Documentación del método definido
# print(MiClase.mi_metodo.__doc__)
# print(MiClase.mi_metodo)
# print(type(MiClase.mi_metodo))
