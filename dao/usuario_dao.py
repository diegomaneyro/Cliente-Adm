from models.conexion import Conexion
from models.cursor_del_pool import CursorDelPool
from models.usuario import Usuario
from config.logger_base import log

class UsuarioDAO:    
    _SELECCIONAR = 'SELECT * FROM usuario'
    _INSERTAR = 'INSERT INTO usuario(id_usuario, username, password) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username= %s, password=%s WHERE id_usuario= %s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'


    # Metodo que devuelve una lista de los objetos usuarios registrados en la db  
    @classmethod
    def seleccionar(cls):
        usuarios = []
        with Conexion.obtenerConexion() as conn:
            with CursorDelPool() as cursor:               
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                for registro in registros:
                    usuario = Usuario(registro[0], registro[1], registro[2])
                    usuarios.append(usuario)
                log.info(f'Usuarios selecionados: {usuarios}')    
        return usuarios


    @classmethod 
    def insertar(cls, usuario):
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valores = (usuario.id_usuario, usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR, valores)
                log.info(f'Usuario insertado: {usuario}')


    @classmethod
    def actualizar(cls, usuario):
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.info(f'Usuario actualizado: {usuario}')

    @classmethod
    def eliminar(cls, usuario):
        with Conexion.obtenerConexion():
            with CursorDelPool() as cursor:               
                valor = (usuario.id_usuario)
                cursor.execute(cls._ELIMINAR, valor)
                log.info(f'usuario eliminado: {usuario}')