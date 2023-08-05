# LAB - Class 33 "Authentication & Production Server"
## Project: django_items
## Author: Ibraheem Areeda


# Setup
- create .env environment : `python -m venv .venv`
- activate the environment : `source .venv/bin/activate`
- to install all requrments : `pip install -r requirements.txt`
- to use the postgresql you mush have docker desktop
- to run the docker : `docker-compose up`

# to initialize/run the application:

to run the server after activating the doker image : `docker-compose run web python manage.py runserver`

# Tests
you can run the tests by `docker-compose run web python manage.py test`
the tests all runing and meets the requirements

### to test API :
For testing manually using thunder client
API Tokens:

Access Token:

method: Post

url: http://127.0.0.1:8000/api/token/ bearer:

    {
        "username": "admin",
        "password": "123",
        "owner": 1
    }

Refresh Token:

method: Post

url: http://127.0.0.1:8000/api/token/refresh/

body:

    {
        {
        "refresh": "Your refresh token"
        }
    }

Api CRUD routes:

    route: http://127.0.0.1:8000/api/v1/items/

## Routes

CRUD Routes for Cookie_stands

Token Required:

    read : no

    creat , update , delet : yes

    api/v1/Cookie_stands/

Create Cookie_stands

HTTP Method: POST

Route: api/v1/Cookie_stands/

Token Required: Yes

Example Request (using ThunderClient):

POST http://127.0.0.1:8000/api/v1/Cookie_stands/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json


Read Cookie_stands

HTTP Method: GET

Route: /api/v1/Cookie_stands/{id}

Token Required: no

Example Request (using ThunderClient):

GET http://127.0.0.1:8000/api/v1/Cookie_stands/1

Update Cookie_stands

HTTP Method: PUT

Route: /api/v1/Cookie_stands/{id}

Token Required: Yes

Example Request (using ThunderClient):

PATHCH http://127.0.0.1:8000/api/v1/Cookie_stands/1
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

Delete Cookie_stands

HTTP Method: DELETE

Route: /api/v1/Cookie_stands/{id}

Token Required: Yes

Example Request (using ThunderClient):

DELETE http://127.0.0.1:8000/api/v1/Cookie_stands/1
Authorization: Bearer YOUR_ACCESS_TOKEN

Example Response:

204 No Content

