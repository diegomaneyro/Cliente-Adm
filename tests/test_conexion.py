import unittest
from models.conexion import Conexion
from config.logger_base import log
from psycopg import OperationalError

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
            self.assertFalse(conexion.closed)
        except OperationalError as e:
            self.fail(f"Error al liberar la conexión: {e}")

if __name__ == '__main__':
    unittest.main()
