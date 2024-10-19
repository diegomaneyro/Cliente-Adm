
"""
Menu de opciones del programa para administrar CRUD en la base de datos usuarios
"""
import sys
from config.logger_base import log
from models.conexion import Conexion
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario

def mostrar_menu():
    print('''
    Menú de Opciones:
    1) Listar usuarios
    2) Agregar usuario
    3) Actualizar usuario
    4) Eliminar usuario
    5) Salir
    ''')

def listar_usuarios():
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        print(f'\nID_usuario: {usuario.id_usuario} - username: {usuario.username} - password: {usuario.password}')

def agregar_usuario():
    username = input('Ingrese username: ')
    password = input('Ingrese password: ')
    usuario = Usuario(username=username, password=password)
    UsuarioDAO.insertar(usuario)
    log.info(f'Usuario agregado: {usuario}')

def actualizar_usuario():
    id_usuario = int(input('Ingrese ID del usuario a actualizar: '))
    username = input('Ingrese nuevo username: ')
    password = input('Ingrese nuevo password: ')
    usuario = Usuario(id_usuario=id_usuario, username=username, password=password)
    UsuarioDAO.actualizar(usuario)
    log.info(f'Usuario actualizado: {usuario}')

def eliminar_usuario():
    id_usuario = int(input('Ingrese ID del usuario a eliminar: '))
    usuario = Usuario(id_usuario=id_usuario)
    UsuarioDAO.eliminar(usuario)
    log.info(f'Usuario eliminado: {usuario}')

def salir_programa():
    log.info('Saliendo del programa')
    Conexion.cerrarConexiones()
    sys.exit()

if __name__ == '__main__':
    while True:
        mostrar_menu()
        try:
            opcion = int(input('\nElija una opción para continuar: '))
        except ValueError:
            print('Por favor, ingrese un número válido')
            continue
        
        if opcion == 1:
            listar_usuarios()
        elif opcion == 2:
            agregar_usuario()
        elif opcion == 3:
            actualizar_usuario()
        elif opcion == 4:
            eliminar_usuario()
        elif opcion == 5:
            salir_programa()
        else:
            print('La opción ingresada no es válida')
