import unittest
from models.conexion import *
from config.logger_base import log
from psycopg import OperationalError

'''
setUpClass y tearDownClass: Métodos para ejecutar acciones antes y después de todas las pruebas,
ideal para inicializar y finalizar el logging.

setUp y tearDown: Métodos que se ejecutan antes y después de cada prueba individual,
útiles para registrar cada inicio y fin de prueba.

Uso de log.info en las pruebas: Para registrar información sobre el estado y el progreso
de las pruebas en los logs, proporcionando detalles adicionales.
'''

class TestConexion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("Iniciando las pruebas de la clase Conexion")

    @classmethod
    def tearDownClass(cls):
        log.info("Finalizando las pruebas de la clase Conexion")
        Conexion.cerrarConexiones()  # Asegurarse de cerrar todas las conexiones al finalizar todas las pruebas

    def setUp(self):
        log.info("Iniciando una prueba...")

    def tearDown(self):
        log.info("Prueba finalizada.")

    def test_obtenerPool(self):
        try:
            pool = Conexion.obtenerPool()
            log.info(f"Pool obtenido: {pool}")
            self.assertIsNotNone(pool, "El pool de conexiones no debería ser None si se creó correctamente")
        except OperationalError as e:
            self.fail(f"Error al obtener el pool de conexiones: {e}")

    def test_obtenerConexion(self):
        try:
            conexion = Conexion.obtenerConexion()
            log.info(f"Conexión obtenida: {conexion}")
            self.assertIsNotNone(conexion)
            Conexion.liberarConexion(conexion)
        except OperationalError as e:
            self.fail(f"Error al obtener la conexión: {e}")

    def test_liberarConexion(self):
        try:
            conexion = Conexion.obtenerConexion()
            log.info(f"Liberando conexión: {conexion}")
            Conexion.liberarConexion(conexion)
            self.assertFalse(conexion.closed)  # Verifica que la conexión no esté cerrada
        except OperationalError as e:
            self.fail(f"Error al liberar la conexión: {e}")

if __name__ == '__main__':
    unittest.main()
