# Django Projects Documentation Site 
A [Django project](https://autodidacticism.herokuapp.com/) that allows me to make blog posts as well as upload pfds/reports about other projects.

## App Hosted in Heroku:
After configuring the Heroku deployment I do not want to have to re-learn how to deploy so I am writing a list of the current process:


Compile Application Through Docker:
```
Build django env from Dockerfile 
Creating Heroku Container for the Docker App: `heroku stack:set container`
Build Docker Image from heroku.yml file that points to Dockerfile
```

Configure Necessary Environment Variables:
```
DJANGO_SETTINGS_MODULE=autodidacticism.heroku_prod_settings
DATABASE_URL
heroku config:set DISABLE_COLLECTSTATIC=1

heroku config: set SECRET_KEY="xxxxxxxxxxxx"
SECRET_KEY for os.getenv('SECRET_KEY')
```

Configure database (postgres):
```
Update DATABASE dev_settings.py params:

import dj_database_url --> dj_database_url.config(conn_max_age=500, ssl_require=True)

DATABASES = {
	'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': BASE_DIR / 'db.sqlite3',
	}

DATABASES['default'].update(prod_db)
```

Perform Database migrations:
```
heroku run python manage.py               
heroku run python manage.py makemigrations     
```

Pushing Changes to Heroku:
```
git push heroku main
```

This should be the laundry list of relevant processes should I need to re-configure the app in heroku. Relevant links that I used for config:

* https://realpython.com/migrating-your-django-project-to-heroku/#convert-from-mysql-to-postgres
* https://devcenter.heroku.com/articles/build-docker-images-heroku-yml#heroku-yml-overview
* https://docs.docker.com/engine/reference/commandline/build/



  

