### В проекте используется БД Postgres. 
* Имя пользователя БД postgres, пароль postgres
Необходимо заранее прописать актуальные имя и пароль в .env или разделе DATABASE в файле setting.py И файле Docker-compose.yml


* Создаем БД и именем d_project ```createdb -U postgres d_project``` (потребуется ввести пароль пользователя postgres)
* Создаем миграции нашего приложения ```python manage.py makemigrations backend```
* Применяем миграции ```python manage.py migrate```
* При необходимости создаем суперпользователя для входа в админку ```python manage.py createsuperuser```
* Создать контейнер ```docker-compose up```

Удалить все временные файлы, что бы пересобрать контейнеер с нуля  ```docker system prune -a```

* Посмотреть задачи celery через Flower ```http://localhost:5555/```
* Админка ```http://localhost:8000/admin/```
* Админ суперюзер:
* login ```mihailoff@inbox.ru```
* password ```diplom```

