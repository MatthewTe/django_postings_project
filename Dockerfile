# Parent Docker Image Python:
FROM python:3.8

# Installing git and necessary system applications:
USER root
RUN apt update && apt install -y git

# Exposing the main port for the wsgi server:
EXPOSE 8000

# Setting the Working Directory:
WORKDIR .

# Copying the django project main directory:
COPY . . 

# Installing all of the necessary python packages:
RUN pip install -r requirements.txt

# Setting the Working Directory to the root of the django project:
WORKDIR django_project/autodidacticism

# Setting Environment variables to Configure Django project:
ENV DJANGO_SETTINGS_MODULE=autodidacticism.heroku_prod_settings

# Performing database migrations at every rebuild:
CMD ['python', 'manage.py', 'makemigrations']
CMD ['python', 'manage.py', 'migrate']

# Running the django server:
CMD ["gunicorn", "autodidacticism.wsgi"]

