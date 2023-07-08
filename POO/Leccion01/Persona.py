class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Jose', 'Perez', 28, '3323232', 2,3,4, m='manzana', p='pera')
persona1.mostrar_detalle() # lo más común

#persona1.telefono = '5500992211'
#print(persona1.telefono)
# Persona.mostrar_detalle(persona1)

persona2 = Persona('Karla', 'Gomez', 30)
persona2.mostrar_detalle()

# persona1.nombre = 'Jose Luis'
# persona1.apellido = 'Martinez'
# persona1.edad = 26
# print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# persona2.nombre = 'Karina'
# persona2.apellido = 'Ramirez'
# persona2.edad = 25
# print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')