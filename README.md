# Reviews Analyzer

Django-Based Web Application

## Running Instructions

### Setup
1 - Install requirements
````
$ pip install -r requirements.txt
````
2 - Configure the database
````
$ python manage.py migrate
````
### Start the project.

In order to run Django
````
$ python manage.py runserver
````

### Setup by Docker (Recommended)
1 - Build application
````
$ docker-compose build
````
2 - Configure database and create super user  
````
$ docker-compose run django bash -c "python manage.py migrate && python manage.py createsuperuser"
````
3 - Start application
````
$ docker-compose up
````

Django is running on: http://localhost:3001
