from config.logger_base import log

class CursorDelPool:
    def __init__(self) -> None:
        self._cursor = None
        self._conn = None

    def __enter__(self):
        try:
            from models.conexion import Conexion
            self._conn = Conexion.obtenerPool().getconn()
            self._cursor = self._conn.cursor()
            return self._cursor
        except Exception as e:
            log.debug(f'Ocurrio un error al obtener el cursor: {e}')
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type or exc_val or exc_tb:
                log.debug(f'Ocurrio un error en la ejecucion: {exc_val}')
                self._conn.rollback()
            else:
                self._conn.commit()
        finally:
            self._cursor.close()
            from models.conexion import Conexion
            Conexion.liberarConexion(self._conn)

            