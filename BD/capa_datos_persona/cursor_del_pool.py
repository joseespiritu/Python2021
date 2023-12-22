from conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._connexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del método with __enter__')
        self._connexion = Conexion.obtenerConexion()
        self._cursor = self._connexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_expecion): # detalle o trackeback (tb)
        log.debug(f'Se ejecuta método __exit__')
        if valor_excepcion:
            self._connexion.rollback()
            log.error(f'Ocurrió una excepción, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_expecion}')
        else:
            self._connexion.commit()
            log.debug(f'Commit de la transacción')
        self._cursor.close()
        Conexion.liberarConexion(self._connexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug(f'Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())