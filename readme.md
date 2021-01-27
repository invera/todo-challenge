# Task Manager web service

- Esta aplicación permite a los usuarios llevar a cabo la gestión y mantenimiento de listas de tareas, o sea que permite crear y eliminar tareas, permite mostrar todas las tareas o una en particular, permite poder modificar sus datos y además cambiar su estado pudiendo tomar uno de los siguientes: Activa, Finalizada o Cancelada. 
- Ademas permite que se realicen busquedas y filtrados mediante fecha de creación y/o contenido de la misma según título o descripción.



## Requerimientos:

- Python 3.7
- Django 3.1.5
- django-filter 2.4.0
- djangorestframework 3.11.1
- djangorestframework-timed-auth-token 1.3.0
- psycopg2-binary 2.8
- Docker y docker-compose



## Instalación y uso:

Para poder correr el proyecto es necesario seguir los siguientes pasos:

- Crear un repositorio en donde alojar el proyecto
- Teniendo instalado Docker y docker-compose ejecutar docker-compose up --build
- Clonar el repositorio a una carpeta de proyectos local.
- Pararse en la rama "master".
- Migrar la base de datos: docker-compose run web python manage.py migrate
- Crear un usuario superuser el cual nos va a permitir poder gestionar las tareas. Para crearlo usar la instrucción: docker-compose run web python manage.py createsuperuser 
- Correr el servior local mediante: docker-compose up
- Importar la colección de postman que se encuentra en la carpeta "postman" para poder correr los endpoints.
- Obtener token del superuser mediante el request que se encuentra en Postman en Account/Account Token. Previamente cambiar los datos de usuario y password por los del usuario recientemente creado.
- En la carpeta "Tarea" de Postman se encuentran todos los requests necesarios para el llamado a los endpoints correspondientes a Tareas. 


## Endpoints:

Todos los endpoint para la gestión de tareas requiere autenticación.

- Crear Token - POST - /api/v1/user/auth/login/
- Crear Tarea - POST - /api/v1/tareas/
- Listar todas las tareas - GET - /api/v1/tareas/
- Listar Tarea por Guid - POST - /api/v1/tareas/[guid]
- Modificación total de Tarea - PUT - /api/v1/tareas/[guid]
- Modificación parcial de Tarea- PATCH - /api/v1/tareas/[guid]
- Eliminar Tarea - DELETE - /api/v1/tareas/[guid]
- Buscar Tarea por rango de fechas de creación - GET - /api/v1/tareas/search/[YYYY-MM-DD]/[YYYY-MM-DD]
- Buscar Tarea por texto en Título o Descripción - GET - /api/v1/tareas/search/[TEXT]
- Buscar Tarea por rango de fechas de creación y por texto en Título o Descripción- GET - /api/v1/tareas/search/[YYYY-MM-DD]/[YYYY-MM-DD]/[TEXT]


## Test:

Esta aplicación contiene un set de pruebas unitarias fundamentalmente para testear los endpoints para la gestión de tareas. Para poder realizar el test correr la siguiente instrucción:

- docker-compose run web python manage.py test


