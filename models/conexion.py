from psycopg2 import pool
from config.logger_base import log
from models.cursor_del_pool import CursorDelPool
import sys

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
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                host = cls._HOST,
                                                user = cls._USERNAME,
                                                port = cls._DB_PORT,
                                                database = cls._DATABASE,
                                                password = cls._PASSWORD
                                                )
                log.debug(f'Se creo el pool de conexiones correctamente')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al crear el pool de conexiones {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = Conexion()
        if cls._pool ==None:
            conexion = cls.obtenerPool().getconn()
            
            try:
                with Conexion() as conexion:
                    with conexion.cursor() as cursor:
                        sentencia = 'SELECT * FROM usuario'
                        cursor.execute()
                        registros = cursor.fetchall(sentencia)
                        log. debug(registros)
            except Exception as e:
                log.debug('ocurrio una excepcion',e)
        else:
            return conexion             

