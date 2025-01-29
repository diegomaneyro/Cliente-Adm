from psycopg_pool import ConnectionPool
from config.logger_base import log
import sys
import os
from dotenv import load_dotenv

load_dotenv()

class Conexion:
    _DATABASE_URL = os.getenv('EXTERNAL_DATABASE_URL')
    _MIN_CON = 1
    _MAX_CON = 6
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = ConnectionPool(conninfo=cls._DATABASE_URL, min_size=cls._MIN_CON, max_size=cls._MAX_CON)                
                log.debug(f'Se creó el pool de conexiones correctamente')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        if cls._pool is None:
            cls.obtenerPool()
        return cls._pool.getconn()

    @classmethod
    def liberarConexion(cls, conexion):
        if cls._pool is not None:
            cls._pool.putconn(conexion)

    @classmethod
    def cerrarConexiones(cls):
        if cls._pool is not None:
            cls._pool.close()
            log.debug('Todas las conexiones del pool han sido cerradas')
        else:
            log.debug('No hay conexiones en el pool para cerrar')
