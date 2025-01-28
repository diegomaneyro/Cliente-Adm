from psycopg_pool import ConnectionPool
from config.logger_base import log
import sys
import os
from dotenv import load_dotenv

load_dotenv()

class Conexion:

    _DATABASE = os.getenv('DB_NAME')
    _USERNAME = os.getenv('DB_USER')
    _PASSWORD = os.getenv('DB_PASSWORD')
    _DB_PORT = os.getenv('DB_PORT')
    _HOST = os.getenv('DB_HOST')
    _MIN_CON = 1
    _MAX_CON = 6
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                conn_str = f"postgresql://{cls._USERNAME}:{cls._PASSWORD}@{cls._HOST}:{cls._DB_PORT}/{cls._DATABASE}"
                cls._pool = ConnectionPool(conninfo=conn_str, min_size=cls._MIN_CON, max_size=cls._MAX_CON)                
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
