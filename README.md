# Read Me

Django uses [Models](https://docs.djangoproject.com/en/4.0/topics/db/models/) to represent database tables

### Setup

For more info on Django check out the [docs](https://docs.djangoproject.com/en/4.0/)

Make sure you have django installed.

The first thing you will need to do is create your database. This is done via [migrations](https://docs.djangoproject.com/en/4.0/).

Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) 
into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, 
when to run them, and the common problems you might run into.


To make and apply migrations:
```shell
python manage.py makemigrations
python manage.py migrate
```

Next you will want to create a user, so you can access the admin page.

To make a superuser:
```shell
python manage.py createsuperuser
```

Now that you have a database setup and a user created, you can start the server


To start the server use:
```shell
python manage.py runserver
```

You can now make changes to your models by changing the models file: 
&nbsp;&nbsp;&nbsp;&nbsp;/the_database_app/models.py


When you are ready to change to a postgres database you can change the database settings
in build_db/settings.py 
 by switching 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
with the below settings (update the name, user, password, host and port). You can make the database
on your local machine or AWS. 
```
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': 'dev_database',
         'USER': 'databaseuser',
         'PASSWORD': 'mypassword',
         'HOST': '127.0.0.0',
         'PORT': '5432',
    }
}
```

Once you get your database as you like, you should delete all of your past migrations and 
do a single, new migration so your SQL is clean. [see example](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

To export the database schema to SQL use: 
```
python manage.py dbshell
> .schema
```
