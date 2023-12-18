import psycopg2 as bd

connexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5433', database='test_db')

# CODIGO CON WITH (AUTOMATICO)
try:
    with connexion:
        with connexion.cursor() as cursor:
            sentence = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            values = ('Alex', 'Rojas', 'arojas@email.com')
            cursor.execute(sentence, values)

            sentence = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            values = ('Juan', 'Perez', 'jperez@email.com', 1)
            cursor.execute(sentence, values)

            print(f'Termina la transaccion, se hizo commit')
except Exception as e:
    print(f'Ocurrió un error, se hizo rollback de la transaccion: {e}')
finally:
    connexion.close()


# CODIGO SIN WITH (MANUAL)
# try:
#     connexion.autocommit = False
#
#     cursor = connexion.cursor()
#     sentence = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
#     values = ('Carlos', 'Lara', 'clara@email.com')
#     cursor.execute(sentence, values)
#
#     sentence = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
#     values = ('Juan Carlos', 'Juarez', 'jcjuarez@email.com', 1)
#     cursor.execute(sentence, values)
#
#     connexion.commit()
#     print(f'Termina la transaccion, se hizo commit')
# except Exception as e:
#     connexion.rollback()
#     print(f'Ocurrió un error, se hizo rollback de la transaccion: {e}')
# finally:
#     connexion.close()
