import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# EJEMPLO CON DELETE
try:
    with conexion:
        with conexion.cursor() as cursor:
            #sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)
            #cursor.execute(sentencia, valores)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros eliminados: {registros_eliminados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

# EJEMPLO CON UPDATE
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#             valores = (
#                 ('Jose', 'Perez', 'jperez@email.com', 1),
#                 ('Ivonne', 'Gutierrez', 'iguitierrez@email.com', 2)
#             )
#             #cursor.execute(sentencia, valores)
#             cursor.executemany(sentencia, valores)
#             registros_actualizados = cursor.rowcount
#             print(f'Registros actualizados: {registros_actualizados}')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     conexion.close()



# EJEMPLO CON INSERT
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
#             valores = (
#                 ('Marcos', 'Cantu', 'mcantu@email.com'),
#                 ('Angel', 'Quintana', 'aquintana@email.com'),
#                 ('Maria', 'Gonzalez', 'mgonzalez@email.com')
#             )
#
#             #cursor.execute(sentencia, valores)
#             cursor.executemany(sentencia, valores)
#             # conexion.commit() # No se debe de ejecutar si se esta utilizando many
#
#             registros_insertados = cursor.rowcount
#             print(f'Registros insertados: {registros_insertados}')
#
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     conexion.close()

# EJEMPLO CON SELECT
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
#             sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
#             #llaves_primarias = ((1,2,3),)
#             entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
#             llaves_primarias = (tuple(entrada.split(',')),)
#
#             # id_persona = input('Proporciona el valor id_persona: ')
#             # cursor.execute(sentencia, (id_persona,))
#
#             cursor.execute(sentencia, llaves_primarias)
#             registros = cursor.fetchall()
#
#             for registro in registros:
#                 print(registro)
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     conexion.close()


