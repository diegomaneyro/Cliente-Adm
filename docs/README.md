# Laboratorio de Usuarios

!(docs/lab_user.jfif)


Este proyecto implementa una aplicación para gestionar usuarios en una base de datos, utilizando operaciones CRUD (Create, Read, Update, Delete). El sistema está diseñado para manejar conexiones a la base de datos a través de un pool de conexiones, y permite realizar transacciones de manera eficiente.

## Base de Datos Utilizada
Este proyecto utiliza **PostgreSQL** para gestionar la base de datos.

## Estructura del Proyecto

### Clases Principales

1. **Conexion**  
   Encargada de manejar la configuración de la conexión a la base de datos. Utiliza un pool de conexiones para optimizar el uso de recursos.
   - **Atributos:**
     - DATABASE: Nombre de la base de datos.
     - USERNAME: Nombre de usuario para la base de datos.
     - PASSWORD: Contraseña del usuario.
     - DB_PORT: Puerto de la base de datos.
     - HOST: Host de la base de datos.
     - MIN_CON: Número mínimo de conexiones en el pool.
     - MAX_CON: Número máximo de conexiones en el pool.
   - **Métodos:**
     - obtenerPool(): Obtiene el pool de conexiones.
     - obtenerConexion(): Obtiene una conexión del pool.
     - liberarConexion(): Libera una conexión de vuelta al pool.
     - cerrarConexiones(): Cierra todas las conexiones.

2. **CursorDelPool**  
   Clase responsable de manejar los cursores de las conexiones obtenidas del pool. Implementa el uso del contexto (with) para trabajar eficientemente con los cursores.
   - **Métodos:**
     - __enter__(): Inicia un contexto con una conexión.
     - __exit__(): Libera la conexión una vez finalizada.

3. **Usuario**  
   Representa la entidad Usuario con los atributos `id_usuario`, `username` y `password`.
   - **Métodos:**
     - __str__(): Representación en cadena del objeto usuario.

4. **UsuarioDao**  
   Realiza las operaciones CRUD sobre la tabla de usuarios en la base de datos.
   - **Constantes SQL:**
     - SELECCIONAR: Consulta para seleccionar todos los usuarios.
     - INSERTAR: Consulta para insertar un nuevo usuario.
     - ACTUALIZAR: Consulta para actualizar un usuario existente.
     - ELIMINAR: Consulta para eliminar un usuario.
   - **Métodos:**
     - seleccionar(): Devuelve una lista de todos los usuarios.
     - insertar(): Inserta un nuevo usuario.
     - actualizar(): Actualiza un usuario existente.
     - eliminar(): Elimina un usuario de la base de datos.

5. **MenuAppUsuario**  
   Define un menú de opciones que permite al usuario realizar las siguientes operaciones:
   - Listar usuarios
   - Agregar usuario
   - Actualizar usuario
   - Eliminar usuario
   - Salir

6. **logger_base**  
   Configura el sistema de logging para toda la aplicación, permitiendo un seguimiento adecuado de las operaciones.

## Tests
Los archivos de pruebas se encuentran en la carpeta `tests`, que contiene los siguientes scripts para validar la funcionalidad del sistema:
- **test_conexion.py**: Pruebas unitarias para la clase Conexion y manejo del pool de conexiones.
- **test_usuario.py**: Pruebas unitarias para la clase Usuario.
- **test_usuario_dao.py**: Pruebas unitarias para la clase UsuarioDao y las operaciones CRUD.

