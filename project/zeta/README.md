### Project name:
Accommodation Web Portal 

### Team name:
WAM84.9

### Team member:
1. Andrew Wirjaputra (Backend + Frontend integration)
2. Shengtao Xu (Frontend)
3. Shiqing Zhang (Frontend)
4. Zhi He (Frontend)

### Build:
> Python 3.6
> Django 2.1

### FOR MAC USERS (using virtual environment)
1. virtualenv venv
2. source venv/bin/activate

### INITIAL SETUP (only once):
1. create a database in postgresql (name it whatever)
2. update DATABASES parameter in zeta/settings.py accordingly (NAME, PASSWORD, etc)
3. pip install django
4. pip install psycopg2
5. pip install django-bootstrap4
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py loaduser
9. python manage.py loaddata listings.json
10. python manage.py loaddata calendars.json
11. python manage.py loaddata reviews.json

### HOW TO RUN:
1. python manage.py runserver
2. Open http://localhost:8000/home
