## Starting 🚀

API for the generation and maintenance of a task list (To-do), encoded in <img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" width="30" height="30" /> !

### Pre-requirements 📋

* Python v3+
* Django
* DjangoRestFramework
* Docker
* Docker-compose

## built with 🛠️

* **Python**
* **Docker**
* **DjangoRestFramework**

## How to test it 📖

If you have Docker installed in your environment, is just that easy to perform the following command at the project path:
<code>docker-compose up -d --build</code>
once it's done, container <strong>config-api_todo</strong> will rise up.

When you're done you can use:

<code>docker-compose down</code>

Then you can follow two ways here, use the preconfigured user or create a new one.

To save your time I would recommend you use the preconfigured user.

<code>{
    "username": "xavelli",
    "password": "hola05"
}</code>

This API works by token authentication, that's the only thing that you would use in order to test it.
So you have the method that create the token (if it doesn't exist)

* **GENERATE THE TOKEN**
<li>
<strong>POST</strong> ⇢ http://127.0.0.1:8000/api_generate_token/
</li>
<li>
<strong>BODY:</strong> <code>{
    "username": "xavelli",
    "password": "hola05"
}</code>
</li>

Will response something like:
<code>
{
    "token": "02de988003985bc2c7b85603e9c0fd20d9f3e9a5"
}
</code>

NOTE: It's the actual token for this user.

Now with this token added to the <strong>Headers</strong> in the next resources, you'll be able to access successfully to them.
The header must be like this:

<code>Authorization : Token 02de988003985bc2c7b85603e9c0fd20d9f3e9a5</code>

* **GET THE LIST OF ALL TO-DOS**
<li>
<strong>GET</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo</code>
</li>


* **GET THE LIST OF specific ID TO-DOS**
<li>
<strong>GET</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo/{id}</code>
</li>

* **GET THE LIST OF specific values**

List of possible values: 

<code>values = ['id', 'title', 'description', 'completed', 'todo_create_date']</code>
* <strong>id: int</strong>
* <strong>title: text</strong>
* <strong>description: text</strong>
* <strong>completed: boolean</strong>
* <strong>todo_create_data: datetime</strong>


<li>
<strong>GET</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo?value={value}</code>
</li>

NOTE: It's by queryString. You can mix your search as much as you like.

* **CREATE A NEW TO-DO**

<li>
<strong>POST</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo</code>
</li>

(The values for your new to-do)

<strong>BODY:</strong> <code>{
    "title": "Title 26",
    "description": "Description test 26",
    "completed": false
}</code>

* **DELETE A TO-DO**

<li>
<strong>DELETE</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo/{id}</code>
</li>

* **UPDATE A TO-DO**

<li>
<strong>PATCH</strong> ⇢ <code>http://127.0.0.1:8000/api/v1/todo/{id}</code>
</li>

(The values for your updated to-do)

<strong>BODY:</strong> <code>{
    "title": "Title edited",
    "completed": true
}</code>

## Version 📌

* **V1**

## Authors ✒️

* **Moises Savelli** - *Developer*

## Expressions of Gratitude 🎁

Thank you Invera, for the opportunity of this CodeChallenge




---
⌨️ With ❤️ by [mxavelli](savellimoises@gmail.com) 😊
