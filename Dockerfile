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

# Running the django server:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
