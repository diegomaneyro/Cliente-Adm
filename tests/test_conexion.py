import unittest
from models.conexion import Conexion

class TestConexion(unittest.TestCase):

    def test_obtenerPool(self):
        pool = Conexion.obtenerPool()
        self.assertIsNotNone(pool, "El pool de conexiones no debería ser None si se creó correctamente")

    def test_obtenerConexion(self):
        conexion = Conexion.obtenerConexion()
        self.assertIsNotNone(conexion)
        Conexion.liberarConexion(conexion)

    def test_liberarConexion(self):
        conexion = Conexion.obtenerConexion()
        Conexion.liberarConexion(conexion)
        self.assertIsNone(conexion.closed)

if __name__ == '__main__':
    unittest.main()
