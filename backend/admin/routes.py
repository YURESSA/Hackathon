import json
import os

from flask import request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from flask_restx import Resource

from backend.core.services.profile_service import *
from . import admin_ns
from ..core.messages import AuthMessages
from ..core.models.hackathon_model import HackathonCase
from ..core.schemas.auth_schemas import login_model, change_password_model, user_model
from ..core.schemas.hackathon_schemas import hackathon_case_model
from ..core.services.hackathon_service import update_hackathon_case, delete_hackathon_case, create_hackathon_case


def admin_required():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return False
    return True


@admin_ns.route('/login')
class AdminLogin(Resource):
    @admin_ns.expect(login_model)
    @admin_ns.doc(description="Аутентификация администратора для получения токена доступа")
    def post(self):
        """Аутентификация администратора для получения токена доступа"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = get_user_by_username(username)
        if not user or not user.check_password(password) or user.system_role.role_name != "admin":
            return {"message": AuthMessages.AUTH_INVALID_CREDENTIALS}, HTTPStatus.UNAUTHORIZED

        access_token = authenticate_user(username, password)
        if access_token:
            return {"access_token": access_token}, HTTPStatus.OK
        return {"message": AuthMessages.AUTH_INVALID_CREDENTIALS}, HTTPStatus.UNAUTHORIZED


@admin_ns.route('/profile')
class AdminProfile(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение информации о пользователе (только для администратора)")
    def get(self):
        """Получение информации о текущем пользователе (только для администратора)"""
        if not admin_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN
        current_username = get_jwt_identity()
        user = get_user_by_username(current_username)
        return get_user_info_response(user)

    @jwt_required()
    @admin_ns.expect(change_password_model)
    @admin_ns.doc(description="Изменение пароля администратора")
    def put(self):
        """Изменение пароля текущего администратора"""
        if not admin_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN
        current_username = get_jwt_identity()
        data = request.get_json()
        if change_password(current_username, data.get("old_password"), data.get("new_password")):
            return {"message": AuthMessages.PASSWORD_CHANGED}, HTTPStatus.OK
        return {"message": AuthMessages.PASSWORD_INVALID_OLD}, HTTPStatus.BAD_REQUEST


@admin_ns.route('/users')
class AdminUserList(Resource):
    @jwt_required()
    @admin_ns.doc(
        description="Получение списка всех пользователей с возможностью фильтрации по роли (только для администратора)")
    @admin_ns.param('role', 'Фильтрация пользователей по роли')
    def get(self):
        """Получение списка всех пользователей с возможностью фильтрации по роли"""
        if not admin_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN

        role_filter = request.args.get('role')
        users = get_all_users(role_filter)

        user_list = [get_user_info_response(u)[0] for u in users]

        return user_list, HTTPStatus.OK

    @jwt_required()
    @admin_ns.expect(user_model)
    @admin_ns.doc(
        description="Создание нового пользователя (жюри/организатора/резидента) от лица администратора или организатора")
    def post(self):
        """Создание нового пользователя (жюри/организатора/резидента)"""
        current_claims = get_jwt()
        creator_role = current_claims.get('role')

        if creator_role not in ["admin", "organizer"]:
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN

        data = request.get_json()
        new_user_role = data.get("role_name")

        if not new_user_role:
            return {"message": "Поле 'role_name' обязательно для создания пользователя."}, HTTPStatus.BAD_REQUEST

        allowed_roles = {
            "admin": ["user", "organizer", "jury"],
            "organizer": ["jury"]
        }

        if new_user_role not in allowed_roles.get(creator_role, []):
            return {"message": f"Вы не можете создать пользователя с ролью '{new_user_role}'."}, HTTPStatus.FORBIDDEN

        return register_user(data)


@admin_ns.route('/users/detail/<string:username>')
class AdminUserDetail(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение информации о пользователе по username (только для администратора)")
    def get(self, username):
        """Получение информации о пользователе по username"""
        if not admin_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN

        user = get_user_by_username(username)
        if user:
            return get_user_info_response(user)
        return {
            "message": AuthMessages.USER_NOT_FOUND}, HTTPStatus.NOT_FOUND

    @jwt_required()
    @admin_ns.doc(description="Удаление пользователя по username (только для администратора)")
    def delete(self, username):
        """Удаление пользователя по username"""
        if not admin_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN

        if delete_user(username):
            return {"message": AuthMessages.USER_DELETED}, HTTPStatus.OK
        return {
            "message": AuthMessages.USER_NOT_FOUND}, HTTPStatus.NOT_FOUND


@admin_ns.route('/hackathon_cases')
class HackathonCaseResource(Resource):
    @jwt_required()
    @admin_ns.expect(hackathon_case_model)
    @admin_ns.doc(description="Создание нового кейса хакатона")
    def post(self):
        """Создать новый кейс хакатона"""
        raw_data = request.form.get("data")
        if not raw_data:
            return {"message": "Поле 'data' (JSON-строка) обязательно."}, HTTPStatus.BAD_REQUEST

        try:
            data = json.loads(raw_data)
        except json.JSONDecodeError:
            return {"message": "Невалидный JSON в поле 'data'."}, HTTPStatus.BAD_REQUEST

        # Получаем файл
        file = request.files.get('file')


        # Создаем новый кейс
        new_case, error, status = create_hackathon_case(data, file)
        if error:
            return error, status

        return {"message": "Кейс успешно добавлен", "case_id": new_case.case_id}, status

    @jwt_required()
    @admin_ns.doc(description="Получение списка всех кейсов хакатона")
    def get(self):
        """Получить список всех кейсов хакатона"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        cases = HackathonCase.query.all()
        case_list = [case.to_dict() for case in cases]
        return {"cases": case_list}, HTTPStatus.OK


@admin_ns.route('/hackathon_cases/<int:case_id>')
class HackathonCaseDetail(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение информации о кейсе хакатона по ID")
    def get(self, case_id):
        """Получить информацию о кейсе хакатона по ID"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        case = HackathonCase.query.get(case_id)
        if not case:
            return {"message": "Кейс не найден."}, HTTPStatus.NOT_FOUND

        return case.to_dict(), HTTPStatus.OK

    @jwt_required()
    @admin_ns.expect(hackathon_case_model)
    @admin_ns.doc(description="Редактирование кейса хакатона")
    def put(self, case_id):
        """Редактировать существующий кейс хакатона"""
        data = request.form.get('data')  # Получаем данные JSON в поле 'data'
        data = json.loads(data)  # Преобразуем в объект Python

        file = request.files.get('file')  # Получаем файл

        case, error, status = update_hackathon_case(case_id, data, file)
        if error:
            return error, status

        return {"message": "Кейс успешно обновлён"}, status

    @jwt_required()
    @admin_ns.doc(description="Удаление кейса хакатона")
    def delete(self, case_id):
        """Удалить кейс хакатона"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        message, status = delete_hackathon_case(case_id)
        return message, status


@admin_ns.route('/download/<string:filename>')
class FileDownload(Resource):
    @jwt_required()
    def get(self, filename):
        """Скачать файл кейса по уникальному имени, но с оригинальным именем при скачивании"""
        upload_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static', 'uploads'))

        # Ищем кейс по file_url (уникальному имени файла)
        case = HackathonCase.query.filter_by(file_url=filename).first()
        if not case:
            return {"message": "Файл не найден."}, 404

        # Получаем оригинальное имя файла из базы данных
        original_filename = case.original_filename

        # Путь к файлу на сервере
        filepath = os.path.join(upload_folder, case.file_url)

        # Проверяем существует ли файл на сервере
        if not os.path.exists(filepath):
            return {"message": "Файл не найден."}, 404

        # Отправляем файл с оригинальным именем
        return send_from_directory(upload_folder, case.file_url, as_attachment=True, download_name=original_filename)
