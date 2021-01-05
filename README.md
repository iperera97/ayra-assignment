# django assignment

technologies
- python 3.7
- django 2.2
- postgresql 10

setup python3
```
apt-get update && apt-get upgrade
apt-get install python3-dev build-essential python3.7-dev  \
                libpq-dev python3-pip libssl-dev \
```

##### project setup
create .env file using .env.example and add environment variables

create virtual environment
```
pipenv shell
```

install packages
```
pipenv sync
```

create tables in database
```
python manage.py migrate
```

add students data to the database
```
python manage.py add_student_data
```

run development server on port 8000
```
python manage.py runserver 8000
```