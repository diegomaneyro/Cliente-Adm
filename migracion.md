# Guía para Migrar tu Proyecto de Terminal a Django

## 1. Instalación de Django

Primero, asegúrate de tener Django instalado en tu entorno virtual. Si no lo tienes instalado, puedes hacerlo con el siguiente comando:

```bash
pip install django
```

## 2. Crear un Proyecto Django

Crea un nuevo proyecto Django. Por ejemplo, si tu proyecto se llama `mi_proyecto`:

```bash
django-admin startproject mi_proyecto
cd mi_proyecto
```

## 3. Crear una Aplicación Django

Dentro de tu proyecto, crea una nueva aplicación. Por ejemplo, si la aplicación se llama `usuarios`:

```bash
python manage.py startapp usuarios
```

## 4. Configurar la Base de Datos

Abre el archivo `settings.py` en la carpeta de tu proyecto y configura la base de datos PostgreSQL. Aquí tienes un ejemplo de configuración:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'tu_host',
        'PORT': 'tu_puerto',
    }
}
```

## 5. Definir los Modelos

Crea el modelo de tu entidad `Usuario` en el archivo `models.py` de la aplicación `usuarios`:

```python
from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
```

## 6. Crear las Migraciones

Genera y aplica las migraciones para crear las tablas en la base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
```

## 7. Crear Vistas y URLs

Define las vistas para manejar las operaciones CRUD en el archivo `views.py` de tu aplicación `usuarios`:

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = Usuario(username=username, password=password)
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/crear_usuario.html')

def actualizar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.username = request.POST['username']
        usuario.password = request.POST['password']
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/actualizar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})
```

Configura las URLs en `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar_usuarios'),
    path('nuevo/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
]
```

## 8. Formularios

Crea formularios para manejar la entrada de datos en `forms.py`:

```python
from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password']
```

## 9. Plantillas

Crea las plantillas HTML en una carpeta `templates/usuarios/` para renderizar las vistas.

---

Con estos pasos, habrás migrado tu proyecto de terminal a un entorno web utilizando Django. Podrás gestionar tus usuarios y realizar operaciones CRUD desde una interfaz web, aprovechando las ventajas que ofrece Django.
