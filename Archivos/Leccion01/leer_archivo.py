# Definir ruta en windows
# archivo = open('C:\\Users\\JoseLuisEspiritu\\Documents\\Programacion\\Python2021\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
# Definir ruta en mac
# archivo = open('C:/Users/JoseLuisEspiritu/Documents/Programacion/Python2021/Archivos/Leccion01/prueba.txt', 'r', encoding='utf8')

archivo = open('prueba.txt', 'r', encoding='utf8')
# print(archivo.read())

# Leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))

# Leer lineas completas
# print(archivo.readline())
# print(archivo.readline())

# Iterar el archivo
# for linea in archivo:
#     print(linea)

# Leer lineas
# print(archivo.readlines())

# Acceder a una linea de la lista
# print(archivo.readlines()[1])

# Abrimos un nuevo archivo
# a - anexar información
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()
print('Se ha terminado el proceso de leer y copiar archivos')