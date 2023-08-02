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

