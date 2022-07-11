FROM python:3.10

ENV AppHome=/usr/tasks-app
RUN mkdir -p $AppHome
WORKDIR ${AppHome}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY . $AppHome
RUN pip install -r requirements.txt

EXPOSE 8080

RUN python manage.py makemigrations tasks_app
RUN python manage.py migrate
RUN python -Wa manage.py test

CMD python manage.py runserver 0.0.0.0:8080
