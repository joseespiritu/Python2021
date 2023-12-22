from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5433'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        connexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {connexion}')
        return connexion

    @classmethod
    def liberarConexion(cls, connexion):
        cls.obtenerPool().putconn(connexion)
        log.debug(f'Regresamos la conexión al pool: {connexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

    # _conexion = None
    # _cursor = None

    # @classmethod
    # def obtenerConexion(cls):
    #     if cls._conexion is None:
    #         try:
    #             cls._conexion = bd.connect(host=cls._HOST,
    #                                        user=cls._USERNAME,
    #                                        password=cls._PASSWORD,
    #                                        port=cls._DB_PORT,
    #                                        database=cls._DATABASE)
    #             log.debug(f'Conexión exitosa: {cls._conexion}')
    #             return cls._conexion
    #         except Exception as e:
    #             log.error(f'Ocurrio una excepcion al obtener la conexión: {e}')
    #             sys.exit()
    #     else:
    #         return cls._conexion

    # @classmethod
    # def obtenerCursor(cls):
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
    #             return cls._cursor
    #         except Exception as e:
    #             log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
    #             sys.exit()
    #     else:
    #         return cls._cursor

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()

    # Conexion.obtenerConexion()
    # Conexion.obtenerCursor()
