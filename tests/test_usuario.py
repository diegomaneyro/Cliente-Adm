import unittest
from models.usuario import Usuario
from config.logger_base import log

class TestUsuario(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info('Iniciando las pruebas de la clase Usuario')

    @classmethod
    def tearDownClass(cls):
        log.info('Finalizando las pruebas de la clase Usuario')

    def setUp(self):
        log.info('Iniciando una prueba... ')

    def test_usuario_inicializacion(self):
        log.info('Provando la inicializacion del Usuario')
        usuario = Usuario(1, 'usuario_prueba','password_prueba')
        self.assertEqual(usuario.id_usuario, 1)
        self.assertEqual(usuario.username, 'usuario_prueba')
        self.assertEqual(usuario.password, 'password_prueba')

    def test_setters_getters(self):
        log.info('Probando los getters del Usuario')
        usuario = Usuario(1, 'usuario_prueba','password_prueba')
        usuario._id_usuario = 2
        usuario._username = 'nuevo_usuario'
        usuario._password = 'nuevo_password'

        self.assertEqual(usuario.id_usuario, 2)
        self.assertEqual(usuario.username, 'nuevo_usuario')
        self.assertEqual(usuario.password, 'nuevo_password')

if __name__ == '__main__':
    unittest.main()
