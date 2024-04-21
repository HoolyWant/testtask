Для запуска потребуется настройка виртуального окружения

        python3 -m venv env
        source env/bin/activate
        pip install -r requirements.txt

Далее следует запустить приложение 

        python3 manage.py runserver

В отдельном терминале запустите Celery, для асинхронной отправки сообщений

        celery worker --app=core --loglevel=info

Для запуска с помощью docker введите команду:
        
        docker-compose up -d --build

Пример для заполнения README

        POSTGRES_DB='test'
        POSTGRES_PASSWORD='qwerty'
        POSTGRES_USER='postgres'
        POSTGRES_HOST='localhost'
        CACHE_ENABLED='True'
        LOCATION='redis://redis:6379/0'
        EMAIL_HOST_USER=почта с которой идет рассылка
        EMAIL_HOST_PASSWORD=данные с сайта почты
        PG_DATA=/var/lib/postgresql/data
        SECRET_KEY='j%+*xd4$@qzwunjaeiwriovqrj)c3$vl#t42ouq$*zt^s4r*b5'

Переменная для хранения адресов для рассылки лежит в [settings.py](config/settings.py) и называется MAILLING_EMAILS

Источник настроен под Яндекс.Почту, но при желании можно поменять параметры SSL и TLS, в зависимости от почтового сервиса

Создание жанра, автора и книг реализовано через админ-панель по адресу /admin. Для создания аккаунта админа следует ввести:

         python3 manage.py createsuperuser 

