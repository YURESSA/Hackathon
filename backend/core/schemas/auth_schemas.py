from flask_restx import fields

from backend.core import api

# Логин
login_model = api.model('Login', {
    'username': fields.String(required=True, description='Ник в Telegram (например, @username)'),
    'password': fields.String(required=True, description='Пароль')
})

# Регистрация
user_model = api.model('User', {
    'username': fields.String(required=True, description='Имя пользователя'),
    'email': fields.String(required=True, description='Электронная почта'),
    'password': fields.String(required=True, description='Пароль'),
    'full_name': fields.String(required=True, description='Полное имя'),
    'phone': fields.String(required=True, description='Телефон'),
    'university': fields.String(required=True, description='ВУЗ'),
    'study_info': fields.String(required=True, description='Информация о курсе и направлении'),
    'role_name': fields.String(required=False, description='Системная роль (например, admin, user, jury)'),
    'project_role': fields.String(required=False, description='Роль пользователя в проекте (может быть пустой)')
})

# Смена пароля
change_password_model = api.model('ChangePassword', {
    'old_password': fields.String(required=True, description='Старый пароль'),
    'new_password': fields.String(required=True, description='Новый пароль')
})

# Поиск по username
username_model = api.model('Username', {
    'username': fields.String(required=True, description='Ник в Telegram (например, @username)')
})

# Фильтрация по роли
user_type_model = api.model('UserType', {
    'role': fields.String(required=True, description='Роль пользователя (Участник, Организатор, Жюри)')
})
