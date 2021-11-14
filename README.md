# ToDoChallenge Invera

![](https://img.shields.io/github/forks/Sanguet/Switch-SPA-APP) ![](https://img.shields.io/github/commit-activity/w/Sanguet/Switch-SPA-APP) ![](https://img.shields.io/github/last-commit/Sanguet/Switch-SPA-APP)

**ToDoChallenge** es un desafio hecho por **Invera**
Puedes consultar la documentacion oficial de este repositorio para conocer mas **[DocumentationOficial](https://ivan-van.gitbook.io/todochallenge/)**

## Inicio 🚀

Estas instrucciones van a proporcionar una ** copia ** de el ** proyecto ** en tu maquina ** local ** para **testear y corroborar** que este todo correcto.

### Pre-requiments 📋

Necesitas installar ** Docker ** y una terminal de Linux, yo recomiendo ** Ubuntu **

```
https://docs.docker.com/docker-for-windows/install/
https://www.itechguides.com/how-to-install-ubuntu-on-windows-10/
```

### Instalation 🔧

Una vez que tienes Docker, la instalacion es super sencilla

El primer paso es clonar el repositorio de GitHub

```
git clone https://github.com/Sanguet/todo-challenge.git
```

El siguiente paso es el directorio donde se encuentra el proyecto

```
cd todo-challenge/
```

Ahora tenemos que ** construir ** los contenedores y imagenes de Docker (puede usar "sudo" si tu terminal lo requiere)

```
docker-compose -f local.yml build
```

Bien, ahora que el entorno esta montado, solo queda hacer las migraciones de la DB

```
docker-compose -f local.yml run --rm django python manage.py migrate
```

Ahora tendras que crear un admin con permisos especiales para acceder al admin Dashboard

```
docker-compose -f local.yml run --rm django python manage.py createsuperuser
```

Ahora tienes todo lo necesario para empezar a usar la API, puedes crear tu propia cuenta en **localhost: 8000/users/signup/ ** y logearte con tus credenciales en **localhost: 8000/users/login/ **

- Tambien puedes mirar la **[OficialDocumentation](https://ivan-van.gitbook.io/switchapidoc/)** y probar esos metodos con **[Postman](https://www.postman.com/)**, o puedes usar este entorno especial de postman **[ColeccionOficial](https://www.mediafire.com/file/kfoiededdmu0qmo/ToDo_Challenge.postman_collection.json/file)**

## Hecho con 🛠️

Esta API esta desarrollada con muchas librerias y frameworks, todo esta explicado en el archivo ** requirements ** , pero estos son los mas importantes

- [Django](https://www.djangoproject.com/) - The framework most used in backend
- [Django REST Framework](https://www.django-rest-framework.org/) - The framework most used to create API REST
- [SimpleJWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) - Used to create and manipulate JWT
- [Celery](https://github.com/celery/celery/) - Used for asynchronous task control and cache management
- [Redis](https://github.com/redis/redis) - Used for cache control
- [Django Anymail](https://github.com/anymail/django-anymail) - Used for manipulating emails

## Autores ✒️

Estas son todas las personas que contribuyeron

- **Oyarzabal Ivan\*** - _Development_ - [Ivan](https://github.com/Sanguet)
- **Oyarzabal Ivan\*** - _Documentation_ - [Ivan](https://github.com/Sanguet)

## Expresiones de gratitud 🎁

-Muchas gracias a ** todas** las personas que decidieron revisar este proyecto 📢

- Y gracias por haber leido hasta aqui, se que es mucho texto 🤓 ..

---

⌨️ con ❤️ por [Ivan](https://github.com/Sanguet) 😊
