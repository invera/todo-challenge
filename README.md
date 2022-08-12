##### ¡IMPORTANTE! #####
\\\\\\\\\\\\\\\\\\\\\\\\

Usuario = lucas
Contraseña= 1234
Token = ced0f281226d8c169a7e7950910f402ebb102062

\\\\\\\\\\\\\\\\\\\\\\\\\
Los campos de los JSON 
"author(user)"
"email(user)"

representan informacion especificada del User, se realizaron con una función toJson en el modelo

\\\\\\\\\\\\\\\\\\\\\\\\\

|Header          |Value
|Authorization	 |Token ced0f281226d8c169a7e7950910f402ebb102062

\\\\\\\\\\\\\\\\\\\\\\\\\

La paginación de los registros es de 15, podes modificarla en ../invera/settings.py 
desplazarte hasta el apartado 
REST_FRAMEWORK
y cambiar el 15 por los valores que quieras.
'PAGE_SIZE': 15,

\\\\\\\\\\\\\\\\\\\\\\\\\


#####


#####


#####
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##### GET de archivos(Postman)

Para ver todos los registros desde terminal con la libreria https(instalada en el entorno)

>>> https http://127.0.0.1:8000/api/tasks/ "Authorization: Token ced0f281226d8c169a7e7950910f402ebb102062"


O podemos hacerlo desde Postman, poniendo en los Headers 

|Header          |Value
|Authorization	 |Token ced0f281226d8c169a7e7950910f402ebb102062

y en la peticion

http://127.0.0.1:8000/api/tasks/  | METHOD= GET

Para ver los registros con las tareas completas:

http://127.0.0.1:8000/api/task/completedlist/ | METHOD= GET

Para ver los usuarios:

http://127.0.0.1:8000/api/userlist/

#####
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
##### Post de archivos(Postman)
 
|Header          |Value
|Authorization	 |Token ced0f281226d8c169a7e7950910f402ebb102062


http://127.0.0.1:8000/api/tasks/  | METHOD= POST

Form Fields

|Field name      |Value
author		 <* pk_User:int > 
name_task	 <texto de ejemplo>
completed        true/false

* pk_User= La primarykey de User es el valor autoasignado por cada registro de usuario en la base de datos, podemos verla a traves de DBrowser:
-auth_user
y se encuentra con un nombre "id", siempre es de caracter int.


Los demás campos se autocompletaran solos con la información del usuario y en el caso de la fecha, tomara la actual al momento de ejecutar la petición.

Form example
http://127.0.0.1:8000/api/tasks/ | METHOD= POST

|Field name      |Value
author		      1 
name_task	     Post con postman
completed        true


y obtendriamos un JSON como este:

{
    "id": 15,
    "author": 2,
    "name_task": "post prueba postman",
    "completed": true,
    "author(user)": "messi",
    "email(user)": "",
    "date_task": "2022-08-12T13:49:32.774752Z"
}




#####
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
##### PUT de archivos(Postman)


|Header          |Value
|Authorization	 |Token ced0f281226d8c169a7e7950910f402ebb102062

Pasamos la siguiente URL especificando la pk de la tarea, este caracter es siempre un int.

http://127.0.0.1:8000/api/tasks/<pk_task:int>/  | METHOD= PUT

Form Fields

|Field name      |Value
author		 <* pk_User:int > 
name_task	 <texto de ejemplo>
completed        true/false


* pk_User= La primarykey de User es el valor autoasignado por cada registro de usuario en la base de datos, podemos verla a traves de DBrowser:
-auth_user
y se encuentra con un nombre "id", siempre es de caracter int.


Los demás campos se autocompletaran solos con la información del usuario y en el caso de la fecha, tomara la actual al momento de ejecutar la petición.


Form example
http://127.0.0.1:8000/api/tasks/7/             | METHOD= PUT

|Field name      |Value
author		 3 
name_task	 Put con postman
completed        true


y obtendriamos un JSON como este:

{
    "id": 7,
    "author": 3,
    "name_task": "post prueba postman PUT",
    "completed": true,
    "author(user)": "cristianoronaldo",
    "email(user)": "cristianoronaldo@gmail.com",
    "date_task": "2022-08-12T04:52:07.683125Z"
}



#####
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
##### DELETE de archivos(Postman)

Header          |Value
|Authorization	 |Token ced0f281226d8c169a7e7950910f402ebb102062

Pasamos la siguiente URL especificando la pk de la tarea, este caracter es siempre un int.

http://127.0.0.1:8000/api/tasks/<pk_task:int>/  | METHOD= DELETE



Form example
http://127.0.0.1:8000/api/tasks/13/ | METHOD= DELETE



y no obtendriamos un JSON porque los campos se borraron :(, pero efectivamente el registro es historia.



#####
++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
##### LOGS

Para visualizar los logs lo haremos dentro del admin


http://127.0.0.1:8000/admin/drf_api_logger/apilogsmodel/

Iniciando sesión con 
Usuario = lucas
Contraseña= 1234


Para ver la aplicacion fronted

http://127.0.0.1:8000
