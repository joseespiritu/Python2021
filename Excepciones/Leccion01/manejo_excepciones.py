from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('números idénticos')
    resultado = a/b
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - Ocurrió un error: {zde}, {type(zde)}')
except TypeError as te:
    print(f'TypeError - Ocurrió un error: {te}, {type(te)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e}, {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución del bloque finally')

print(f'Resultado: {resultado}')
print('Continuamos...')

