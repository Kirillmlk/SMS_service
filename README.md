# Сервис уведомлений

Сервис разработан на django rest framework с celery

## Установка и запуск

1. Склонировать репозиторий с Github:

2. Перейти в директорию проекта

3. Создать виртуальное окружение:

```
python -m venv venv
```

4. Активировать окружение:

```
source\venv\bin\activate
```

5. В файле .evn заполнить необходимые данные: `TOKEN = '<your token>`

6. Установка зависимостей:

```
pip install -r requirements.txt
```

7. Создать и применить миграции в базу данных:

```
python manage.py makemigrations
python manage.py migrate
```

8. Запустить сервер

```
python manage.py runserver
```

***

```http://127.0.0.1:8000/api/clients``` - получить всех клиентов
```http://127.0.0.1:8000/api/mailing``` - получить все рассылки




