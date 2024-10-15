class Usuario:
    contador_usuarios = 0
    def __init__(self, username: str, password: str):
        Usuario.contador_usuarios += 1
        self._id_usuario = Usuario.contador_usuarios
        self._username = username
        self._password = password

    def __str__(self):
        return f'Id_usuario: {self._id_usuario}, username: {self._username}, password: {self._password}'

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
