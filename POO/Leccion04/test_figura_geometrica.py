from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creación objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(lado = -10, color =  'rojo')
cuadrado1.alto = -10
print(cuadrado1)
print(f'Cálculo del área cuadrado: {cuadrado1.calcular_area()}')

print('Creación objeto rectangulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho = 12, alto = 5, color = 'verde')
rectangulo1.ancho = 15
print(rectangulo1)
print(f'Cálculo del área rectangulo: {rectangulo1.calcular_area()}')



print('Method Resolution Order example'.center(50, '-'))
# MRO - Method Resolution Order
print(Cuadrado.mro())