FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 9000

WORKDIR /code

RUN apt-get update && apt-get install -y gcc libjpeg-dev libpq-dev

RUN pip install -upgrade pip

COPY ./requirements.txt /code/requirements.txt

RUN pip install -no-cache-dir upgrade -r /code/requirements.txt

COPY . .

ENTRYPOINT python manage.py migrate & python manage.py runserver 0.0.0.0:8000




