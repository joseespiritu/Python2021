from ManejoArchivos import ManejoArchivos


'''
    Con with se abstraen dos funciones de la clase object
    __enter__
    __exit__
    Context Manager - Administrador de recursos
'''
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())
