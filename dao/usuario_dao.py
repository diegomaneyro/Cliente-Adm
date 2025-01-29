from models.conexion import Conexion
from models.cursor_del_pool import CursorDelPool
from models.usuario import Usuario
from config.logger_base import log

class UsuarioDAO:
    """
    Clase DAO (Data Access Object) para la entidad Usuario.
    Maneja operaciones CRUD para los objetos Usuario en la base de datos.
    """
    _SELECCIONAR = 'SELECT * FROM usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username= %s, password=%s WHERE id_usuario= %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        """
        Selecciona todos los registros de la tabla usuario.
        
        :return: Lista de objetos Usuario.
        """
        usuarios = []
        with Conexion.obtenerConexion() as conn:
            with CursorDelPool() as cursor:               
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                for registro in registros:
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    usuarios.append(usuario)
                log.info(f'Usuarios seleccionados: {usuarios}')    
        return usuarios

    @classmethod 
    def insertar(cls, usuario):
        """
        Inserta un nuevo registro en la tabla usuario.
        
        :param usuario: Objeto Usuario a insertar.
        """
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.info(f'Usuario insertado: {usuario}')

    @classmethod
    def actualizar(cls, usuario):
        """
        Actualiza un registro existente en la tabla usuario.
        
        :param usuario: Objeto Usuario con los nuevos datos.
        """
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.info(f'Usuario actualizado: {usuario}')

    @classmethod
    def eliminar(cls, usuario):
        """
        Elimina un registro de la tabla usuario.
        
        :param usuario: Objeto Usuario a eliminar.
        """
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valor = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valor)
                log.info(f'Usuario eliminado: {usuario}')
