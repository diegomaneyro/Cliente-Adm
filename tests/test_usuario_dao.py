import unittest
from models.usuario import Usuario
from dao.usuario_dao import UsuarioDAO
from config.logger_base import log

class TestUsuarioDAO(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log.info("Iniciando las pruebas de la clase UsuarioDAO")

    @classmethod
    def tearDownClass(cls):
        log.info("Finalizando las pruebas de la clase UsuarioDAO")

    def setUp(self):
        log.info("Iniciando una prueba...")

    def tearDown(self):
        log.info("Prueba finalizada.")

    def test_insertar(self):
        usuario = Usuario(1, 'usuario_test', 'password_test')
        UsuarioDAO.insertar(usuario)
        log.info(f'Insertar prueba: {usuario}')

    def test_seleccionar(self):
        usuarios = UsuarioDAO.seleccionar()
        log.info(f'Seleccionar prueba: {usuarios}')
        self.assertGreater(len(usuarios), 0)  # Verifica que se haya seleccionado al menos un usuario

    def test_actualizar(self):
        usuario = Usuario(1, 'usuario_actualizado', 'password_actualizado')
        UsuarioDAO.actualizar(usuario)
        log.info(f'Actualizar prueba: {usuario}')

    def test_eliminar(self):
        usuario = Usuario(1, 'usuario_actualizado', 'password_actualizado')
        UsuarioDAO.eliminar(usuario)
        log.info(f'Eliminar prueba: {usuario}')
        usuarios = UsuarioDAO.seleccionar()
        user_ids = [user.id_usuario for user in usuarios]
        self.assertNotIn(usuario.id_usuario, user_ids)

if __name__ == '__main__':
    unittest.main()
