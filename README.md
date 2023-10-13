# BlogVoyage + REST API (BlogVoyage.API)
## _Social network for bloggers and even more_
## based on:
[![N|Solid](https://static.djangoproject.com/img/logos/django-logo-negative.svg)](https://www.djangoproject.com/)
## and
[![N|Solid](https://www.django-rest-framework.org/img/logo.png)](https://www.django-rest-framework.org/)

BlogVoyage is a project for learning, testing and improving skills on python, django, sql, REST api etc.

## Features*
Does not contain web responses, html web pages rendering etc. It is projected to use with frontend module via SPA technology (using json exchange of data)
Images will be transfered as a binary Base64 image format.
*more of them will be implemented up to 15 Oct. 2023

- Could start a DEV server
- Could post, update, delete posts, groups, commentaries via API

## Tech

BlogVoyage uses a number of open source projects to work properly:

- [Python] - Python 3.9
- [Django] - Web framework to rule them all!
- [Django Rest Framework (DRF)] - REST API support for Django
- [Simple JWT (DRF JWT)] - Django Rest Framework Simple JWT Token authentication backend


And of course BlogVoyage itself is open source with a [public repository][Rexant-b2k]
 on GitHub.

## Installation

BlogVoyage requires [Django] v3.2.16 to run.

Install the dependencies and devDependencies and start the server (Linux/MacOS example).

```sh
python -m pip install --upgrade pip
python -m venv venv
source venv/bin/activate
```

For production environments (automatic)...

```sh
pip install -r requirements.txt
```
or manual:
```sh
pip install Django==3.2.16
pip install djangorestframework
```

## Making migrations
```sh
venv..$ .../BlogVoyage_api: python manage.py migrate
```

## Running server
```sh
venv..$ .../BlogVoyage_api: python manage.py runserver
```

##### Information about possible request are available at **http://127.0.0.1:8000/redoc/ in your browser**

## Requests example
*Could be done using Postman or another simular app, or via browser.
###### Get posts list:
Request:
```cmd
http://127.0.0.1:8000/api/v1/posts/
```
Response:
```sh
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
###### Make commentary:
Request:
```cmd
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```
```sh
{
    "text": "string"
}
```

Response:
```sh
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

## Plugins

BlogVoyage is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dillinger | [https://dillinger.io/][Dill] |

## Docker

The information will be available in future.


## License

BSD-3 Clause License

**Free Software, Hello everybody**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Rexant-b2k]: <https://github.com/Rexant-b2k>
   [git-repo-url]: <https://github.com/Rexant-b2k/BlogVoyage_api.git>
   [Django]: <https://www.djangoproject.com>
   [Python]: <https://www.python.org/>
   [Django Rest Framework (DRF)]: <https://www.django-rest-framework.org/>
   [Simple JWT (DRF JWT)]: <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>


   [Dill]: <https://dillinger.io/>
