from psycopg2 import pool
from logger_base import log

class Conexion:

    _DATABASE = 'persona'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None


@classmethod
def obtenerPool(cls):
    if pool is None:
        try:
            cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                            host = cls._HOST,
                                            user = cls._USERNAME,
                                            port = cls._DB_PORT,
                                            database = cls._DATABASE,
                                            password = cls._PASSWORD
                                            )
            log.deb(f'Se creo el pool de conexiones correctamente {cls._pool}')
        except Exception as e:
            log.error(f'Ocurrio un error al crear el pool d conexiones {e}')
    else:
        return cls._pool

@classmethod
def obtenerConexion(cls):
    pass
