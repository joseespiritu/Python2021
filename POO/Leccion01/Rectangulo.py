class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Proporciona la base: '))
altura = int(input('Proporciona la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectangulo1: {rectangulo1.calcular_area():.2f}')