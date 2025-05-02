# Hackathon Management Platform

Веб-приложение для управления хакатоном, реализованное на Flask.

## Основной функционал

### Роли пользователей
- **Админ**: управление пользователями, создание организаторов и жюри.
- **Организатор**: управление командами, кейсами, жюри.
- **Жюри**: просмотр артефактов команд, выставление оценок и отзывов.

### Участники и команды
- Регистрация пользователей.
- Создание и управление командами.
- Отправка артефактов (GitHub, Figma, презентации и пр.).

### Оценка проектов
- Жюри оценивает команды по 5 критериям.
- Оставление текстового фидбека.

### API (Flask-RESTx)
- Пространства имён: `/admin`, `/organizer`, `/jury`, `/teams`, и др.
- JWT-аутентификация.
- Ролевой доступ.

## Установка

```bash
git clone https://github.com/YURESSA/hackathon-platform.git
cd hackathon-platform
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask db upgrade
flask run
```

## Стек технологий

- Python 3.10+
- Flask + Flask-RESTx
- SQLAlchemy
- JWT (Flask-JWT-Extended)
- PostgreSQL / SQLite
- Swagger-документация API
