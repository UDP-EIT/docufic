# Docufic | Repositorio de archivos

Repositorio para el proyecto Docufic del Centro de Alumnos de la Facultad de Ingeniería de la Universidad Diego Portales. Realizado en Django.

**Última actualización**: 09/08/2020

### Requisitos

- Python 3.6+
- Pip 20.0.0+
- Postgres 10.0+

### Instalación
Clonar el repositorio. Crear un entorno virtual (Opcional) e instalar `pip`, para instalar los requerimientos de la siguiente manera:
```
pip install -r requirements.txt
```

En una consola para el usuario `postgres`, crear la base de datos:
`create database docuficbdd;`
Después, crear un usuario (Opcional) y realizar configuraciones básicas:
```
create user docuficuser with password 'docufic123';
alter role docuficuser set client_encoding to 'utf8';
alter role docuficuser set default_transaction_isolation to 'read committed';
alter role docuficuser set timezone to 'GMT-4';
```
Luego, asignar los privilegios correspondientes.
```
grant all privileges on database docuficbdd to docuficuser;
```
Finalmente, correr las migraciones e iniciar el servidor local. Dentro del entorno virtual (O del interprete utilizado) y desde el directorio principal (Donde se ubica manage.py):
```
python manage.py migrate
python manage.py makemigrations core
python manage.py migrate
python manage.py runserver
```

Para acceder al sitio, acceder de forma local mediante http://127.0.0.1:8000
El panel de administración se ubica en http://127.0.0.1:8000/admin


### Estructura
La estructura del proyecto está predefinida por `Django Framework`. A continuación se detallan las principales funciones de los archivos y su ubicación.

Core:
- **views.py**: Contiene toda la lógica detrás de cada `request` y cada función o clase es la responsable de responder con un `render`.
- **urls.py**: Cada función o clase de `views.py` es asociada con una `URL` y un nombre, a fin de ser referenciada si es necesario.
- **admin.py**: Modifica el despliegue de la información por defecto de los modelos en el panel de administración.

Docufic:
- **settings.py**: Archivo principal del proyecto en el que se ubican las constantes, instalaciones y configuraciones que afectan de manera global el proyecto.
- **urls.py**: Permite importar y asociar a diversas `URL` de manera global, las otras definidas en el resto de aplicaciones. En el caso de `Core`, dichas direcciones se asignan a `/`.


### Organización de templates
Todas las respuestas se hacen con `render`. Las plantillas base se ubican en `core/templates/`, luego, las plantillas que heredan de estas se encuentran en `core/templates/core`.
Plantillas disponibles:
- **base.html**: Contiene los imports para fuentes, componentes visuales y algunos elementos que interactuan con el DOM. Su principal función es contener el `header` y el `footer`
- **core/index.html**: Página principal. Se ubica aquí el buscador y la imagen principal.
- **core/ramo.html**: Página de visualización de ramo. Se despliegan todos los atributos de un objeto de modelo `Ramo`.


### Commits

No se ha utilizado una notación en específico.




