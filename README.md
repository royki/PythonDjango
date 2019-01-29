#### _Platform_
--------------
- Python v3.6
- Django 1.11.7

#### _Execution_
----------------
- `python manage.py migrate`
- 'python manage.py runserver'

##### Create User
-----------------
- `python manage.py createsuperuser`

#### _URL_
----------
- `http://127.0.0.1:8000` => Welcome
- `http://127.0.0.1:8000/time/` => Current Time 
- `http://127.0.0.1:8000/time/plus/5/` # Any 2 digit number => Current Time + Digit
- `http://127.0.0.1:8000/authors/` => List of Authors, Books and Publisher
- `http://127.0.0.1:8000/search-form/` => Small Search Template
