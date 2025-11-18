# Q&A API Service

Тестовое задание. Простой сервис вопросов и ответов на Django REST Framework с PostgreSQL и Docker.

## Описание проекта

Проект предоставляет REST API для работы с вопросами (Question) и ответами (Answer).
Пользователи могут:
* Создавать, получать и удалять вопросы.
* Добавлять, получать и удалять ответы к вопросам.
* Один пользователь может оставлять несколько ответов к одному вопросу.
* При удалении вопроса все ответы удаляются каскадно.

В проекте реализованы валидация данных (проверка пустого текста и корректности UUID) и логгирование действий. Тестирование выполнено с использованием pytest, проверка запросов - через Postman, а данные в БД - через DBeaver.

### Технологии:
* Python 3.12
* Django 5
* Django REST Framework
* PostgreSQL 16
* Docker + docker-compose
* Pytest для тестирования
* Logging для отслеживания действий и запросов

### Структура проекта


```
hightalent/
├── hightalent_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── questions/
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── serializers.py
│       ├── validators.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
├── tests/
│   ├── conftest.py
│   ├── test_answers.py
│   └── test_questions.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── .env
```

* `questions/` — приложение с моделями, сериализаторами, валидаторами, views и маршрутизацией.
* `tests/` — тесты API с использованием pytest и DRF APIClient.
* Dockerfile и docker-compose.yml — контейнеризация сервиса и базы данных.
* .env — переменные окружения (доступ к БД, секретный ключ, debug).

### Установка и запуск
1. Клонировать репозиторий:

```bash
git clone <repo_url>
cd hightalent
```

2. Создать .env файл с примером:

```text
POSTGRES_DB=questions_db
POSTGRES_USER=questions_user
POSTGRES_PASSWORD=questions_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
DJANGO_SECRET_KEY=django-insecure-test-secret
DJANGO_DEBUG=True
```

3. Если образы Python или PostgreSQL не скачаны, выполнить:

```bash
docker pull python:3.12-slim
docker pull postgres:16
```

4. Запустить сервис через Docker Compose:

```bash
# В обычном режиме (видны логи)
docker-compose up --build

# В фоне (detached mode)
docker-compose up -d --build
```

5. Приложение будет доступно по адресу: http://localhost:8000/.
6. Применить миграции (если нужно):

```commandline
docker-compose exec web python manage.py migrate
```

### Примеры API

Вопросы
* GET /questions/ — список всех вопросов
* POST /questions/ — создать вопрос

`POST /questions/`
```json
{
  "text": "Что такое Django?"
}
```

* GET /questions/{id}/ — получить вопрос с ответами
* DELETE /questions/{id}/ — удалить вопрос и все ответы

Ответы
* POST /questions/{id}/answers/ — добавить ответ к вопросу

`POST /questions/1/answers/`
```json
{
  "user_id": "a1b2c3d4-5678-90ab-cdef-1234567890ab",
  "text": "Это фреймворк для веб-разработки на Python"
}
```

* GET /answers/{id}/ — получить конкретный ответ
* DELETE /answers/{id}/ — удалить ответ

### Тестирование

Запуск тестов:

```bash
docker-compose exec web pytest
```
