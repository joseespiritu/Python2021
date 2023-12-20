from conexion import Conexion
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
        DAO (Data Access Object)
        CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as connexion:
            with connexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registers = cursor.fetchall()
                people = []
                for register in registers:
                    person = Persona(register[0], register[1], register[2], register[3])
                    people.append(person)
                return people

    @classmethod
    def insertar(cls, person):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                values = (person.nombre, person.apellido, person.email)
                cursor.execute(cls._INSERTAR, values)
                log.debug(f'Persona agregada: {person}')
                return cursor.rowcount

    @classmethod
    def actualizar(cls, person):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                values = (person.nombre, person.apellido, person.email, person.id_persona)
                cursor.execute(cls._ACTUALIZAR, values)
                log.debug(f'Persona actualizada: {person}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls, person):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                values = (person.id_persona,)
                cursor.execute(cls._ELIMINAR, values)
                log.debug(f'Objeto eliminado: {person}')
                return cursor.rowcount

if __name__ == '__main__':
    # Insertar un registro
    # persona1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@email.com')
    # people_add = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas agregadas: {people_add}')

    # Actualizar un registro
    # persona1 = Persona(1, 'Juan Carlos', 'Juarez', 'jcjuarez@email.com')
    # people_updated = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {people_updated}')

    # Eliminar un registro
    persona1 = Persona(id_persona=14)
    people_deleted = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {people_deleted}')

    # Seleccionar objetos
    people = PersonaDAO.seleccionar()
    for person in people:
        log.debug(person)
