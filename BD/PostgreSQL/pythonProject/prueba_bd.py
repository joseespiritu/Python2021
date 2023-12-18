import psycopg2

connexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5433',database='test_db')

# OBTENER REGISTROS
# try:
#     with connexion:
#         with connexion.cursor() as cursor:
#             sentence = 'SELECT * FROM persona WHERE id_persona IN %s'
#             # llaves_primarias = ((1,2),)
#             entrada = input('Proporciona los id\'s a buscar (separado por comas): ')
#             llaves_primarias = (tuple(entrada.split(',')),)
#             # id_persona = input('Proporciona el valor id_persona: ')
#             # cursor.execute(sentence, (id_persona,))
#             cursor.execute(sentence, llaves_primarias)
#             registers = cursor.fetchall()
#             for register in registers:
#                 print(register)
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     connexion.close()

# INSERTAR REGISTROS, el commit se hace automaticamente con el with
# try:
#     with connexion:
#         with connexion.cursor() as cursor:
#             sentence = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
#             # values = ('Carlos', 'Lara', 'clara@email.com')
#             # cursor.execute(sentence, values)
#             values = (
#                 ('Marcos', 'Cantu', 'mcantu@email.com'),
#                 ('Angel', 'Quintana', 'aquintana@email.com'),
#                 ('Maria', 'Gonzalez', 'mgonzalez@email.com')
#             )
#             cursor.executemany(sentence, values)
#             # connexion.commit()
#             registers_inserted = cursor.rowcount
#             print(f'Registros insertados: {registers_inserted}')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     connexion.close()

# ACTUALIZAR REGISTROS
# try:
#     with connexion:
#         with connexion.cursor() as cursor:
#             sentence = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#             values = (
#                 ('Juan', 'Perez2', 'jperez2@email.com', 1),
#                 ('Ivonne', 'Gutierrez', 'igutierrez@email.com', 2)
#             )
#             # cursor.execute(sentence, values)
#             cursor.executemany(sentence, values)
#             registers_updated = cursor.rowcount
#             print(f'Registros actualizados: {registers_updated}')
# except Exception as e:
#     print(f'Ocurrió un error: {e}')
# finally:
#     connexion.close()


# ELIMINAR REGISTROS
try:
    with connexion:
        with connexion.cursor() as cursor:
            # sentence = 'DELETE FROM persona WHERE id_persona=%s'
            sentence = 'DELETE FROM persona WHERE id_persona in %s'
            entrance = input('Proporciona los id_persona a eliminar (separados por coma): ')
            values = (tuple(entrance.split(',')),)
            cursor.execute(sentence, values)
            registers_deleted = cursor.rowcount
            print(f'Registros eliminados: {registers_deleted}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    connexion.close()