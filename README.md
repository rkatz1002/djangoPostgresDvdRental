# djangoPostgresDvdRental

This project is a simple gist. In this gist we will use django's built in tools to deal with legacy databases, integrate the databases user to django's user, and then write a couple o function api's.

## Set up

### Import data from PostgreSQL dvdrental

The dvdrental is a database which was created to demonstrate the features of the PostgreSQL database.
You can find the files for this [here](https://www.postgresqltutorial.com/postgresql-sample-database/).

### Restore Database

After you download the database you will have to restore it with PostgreSQL commands. To do that, you have to:

- Create a database via command 1;
- Restore the database via command 2 or via pgadmin;

Command 1: `CREATE DATABASE dvdrental;`

Command 2: `pg_restore --dbname=dvdrental --create --verbose path_to\dvdrental.tar`

You can also do command 2 using _pgadmin_. This is all explained [here](https://www.postgresqltutorial.com/postgresql-restore-database/).

### Fix the database

This database isn't so perfect and lacks some columns to adapt it do django user, to fix this you can use the following commands:

`ALTER TABLE staff ALTER COLUMN password TYPE varchar(500);`

`UPDATE staff SET is_staff='t';`

### Install all files in requirements.txt

Use the following command to install all libraries in the requirements.txt file:

`pip install -r requirements.txt`

### Migrate the database

Make sure that, before you make your migrations, you migrate the database to get django's already important tables. To do this, all you have to do is:

`python manage.py migrate`

### Migrate all tables

After you've migrated django's tables, you can migrate your new database:

`python manage.py makemigrations`
`python manage.py migrate`

