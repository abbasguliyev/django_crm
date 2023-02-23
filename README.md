# django_crm

- Configuration
    - create .env file in app and main folders
    - Copy and paste the contents of the env file into the .env file 
- Start without docker
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver
- Start with docker
    - docker-compose build
    - docker-compose run --rm web python3 manage.py createsuperuser
    - docker-compose up
