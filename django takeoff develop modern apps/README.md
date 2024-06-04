# django takeoff develop modern apps

## Create Project
>django-admin startproject example .

## Create Django App
>python3 manage.py startapp listings


## Install Postgres on local system
>sudo apt-get install postgresql

## Start postgres service
>sudo service postgresql restart

## start postgres


## Step 1: Create Database and User

First, access the PostgreSQL prompt. You can do this by running:
>sudo su - postgres
>psql

Then, execute the following SQL commands to create a new database and user:

```bash
##Create the database
CREATE DATABASE my_django_db;

##Create the user
CREATE USER my_django_user WITH PASSWORD 'my_secure_password';

##Grant privileges to the user
GRANT ALL PRIVILEGES ON DATABASE my_django_db TO my_django_user;

##Optionally, you might want to set some additional permissions or configurations
ALTER USER my_django_user CREATEDB;
```

