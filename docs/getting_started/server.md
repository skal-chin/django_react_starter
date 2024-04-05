#### Starting the server

CD into the root directory and run the following commands to build the database.

```bash
cd django-rest-starter

python manage.py makemigrations
python manage.py migrate
```

You can create a superuser to access the admin panel.

```bash
python manage.py createsuperuser
```

Finally, run the server.

```bash
python manage.py runserver
```