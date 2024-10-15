'''
Menu de opciones del programa paara administrar CRUD 
en la base de datos usuarios
'''

import sys
from config.logger_base import log
from models.conexion import Conexion
from dao.usuario_dao import UsuarioDAO
from models.usuario import Usuario


salir = False
while salir is not None:
    print('''Menu de Opciones
        Ingrese una opcion (1-5)
        1) Listar usuarios
        2) Agregar usuario
        3) Actualizar usuario
        4) Eliminar usuario
        5) Salir''')
    opcion = int(input('Elija una opcion para continuar: '))
    if opcion is not 5:
        
        if opcion == 1:
            usuarios = UsuarioDAO.seleccionar()
            for usuario in usuarios:
                print(f'ID_usuario: {usuario.id_usuario} -  username: {usuario.username} - password: {usuario.password}')
        
        elif opcion == 2:
            username = input('Ingrese username: ')
            password = input('Ingrese password: ')
            usuario = Usuario(username = username, password = password)
            UsuarioDAO.insertar(usuario)
                    
        elif opcion == 3:
            pass
        elif opcion == 4:
            id = int(input('Ingrese id_usuario para eliminar: '))
            usuario = Usuario(id_usuario = id)
            UsuarioDAO.eliminar(usuario)
        else:
            print('La opcion ingresada no es valida')
    else:
        log.info('Saliendo del programa')
        Conexion.cerrarConexiones()    
        sys.exit()    
    