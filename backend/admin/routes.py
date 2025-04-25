import json
import os

from flask import request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from flask_restx import Resource

from backend.core.services.profile_service import *
from . import admin_ns
from ..core.messages import AuthMessages
from ..core.models.hackathon_model import HackathonCase
from ..core.models.team_models import Team
from ..core.schemas.auth_schemas import login_model, change_password_model, user_model
from ..core.schemas.hackathon_schemas import hackathon_case_model
from ..core.services.hackathon_service import update_hackathon_case, delete_hackathon_case, create_hackathon_case, \
    assign_cases_evenly


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

        file = request.files.get('file')

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

        if not os.path.exists(filepath):
            return {"message": "Файл не найден."}, 404

        return send_from_directory(upload_folder, case.file_url, as_attachment=True, download_name=original_filename)


@admin_ns.route('/assign_cases')
class AssignCases(Resource):
    @jwt_required()
    @admin_ns.doc(description="Распределение кейсов среди команд (только для администратора)")
    def post(self):
        """Распределение кейсов среди команд"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        result, status = assign_cases_evenly()
        return result, status


@admin_ns.route('/teams')
class TeamList(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение списка всех команд (только для администратора)")
    def get(self):
        """Получить список всех команд"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        teams = Team.query.all()
        team_list = [team.to_dict() for team in teams]
        return {"teams": team_list}, HTTPStatus.OK


@admin_ns.route('/teams/<string:team_name>')
class TeamDetail(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение информации о команде по названию (только для администратора)")
    def get(self, team_name):
        """Получить информацию о команде по названию"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        team = Team.query.filter_by(team_name=team_name).first()  # Поиск по названию
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        return team.to_dict(), HTTPStatus.OK


@admin_ns.route('/teams/<string:team_name>/members')
class TeamMembers(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение списка членов команды по названию (только для администратора)")
    def get(self, team_name):
        """Получить список членов команды по названию"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        team = Team.query.filter_by(team_name=team_name).first()  # Поиск по названию
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        # Члены команды
        members = [member.to_dict() for member in team.members]
        return {"members": members}, HTTPStatus.OK

    @jwt_required()
    @admin_ns.doc(description="Добавление члена в команду по названию (только для администратора)")
    @admin_ns.param('user_id', 'ID пользователя для добавления')
    def post(self, team_name):
        """Добавить нового члена в команду по названию"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        user_id = request.args.get('user_id')
        team = Team.query.filter_by(team_name=team_name).first()  # Поиск по названию
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        user = User.query.get(user_id)
        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        # Добавляем пользователя в команду
        if user not in team.members:
            team.members.append(user)
            db.session.commit()
            return {"message": "Пользователь успешно добавлен в команду."}, HTTPStatus.OK
        return {"message": "Пользователь уже является членом команды."}, HTTPStatus.BAD_REQUEST

    @jwt_required()
    @admin_ns.doc(description="Удаление члена из команды по названию (только для администратора)")
    @admin_ns.param('user_id', 'ID пользователя для удаления')
    def delete(self, team_name):
        """Удалить члена из команды по названию"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        user_id = request.args.get('user_id')
        team = Team.query.filter_by(team_name=team_name).first()  # Поиск по названию
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        user = User.query.get(user_id)
        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        # Удаляем пользователя из команды
        if user in team.members:
            team.members.remove(user)
            db.session.commit()
            return {"message": "Пользователь успешно удалён из команды."}, HTTPStatus.OK
        return {"message": "Пользователь не является членом команды."}, HTTPStatus.BAD_REQUEST


@admin_ns.route('/jury')
class JuryList(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение списка всех членов жюри")
    def get(self):
        """Получить список всех членов жюри"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        # Получаем роль "jury"
        jury_role = Role.query.filter_by(role_name="jury").first()
        if not jury_role:
            return {"message": "Роль 'jury' не найдена."}, HTTPStatus.NOT_FOUND

        # Получаем всех пользователей с этой ролью
        jury_members = User.query.filter_by(system_role_id=jury_role.role_id).all()
        jury_list = [user.to_dict() for user in jury_members]
        return {"jury": jury_list}, HTTPStatus.OK

    @jwt_required()
    @admin_ns.expect(user_model)
    @admin_ns.doc(description="Добавление члена в жюри")
    def post(self):
        """Добавить нового члена в жюри"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        data = request.get_json()
        user = get_user_by_username(data.get('username'))
        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        # Проверяем, является ли пользователь уже членом жюри
        if user.system_role.role_name == "jury":
            return {"message": "Пользователь уже является членом жюри."}, HTTPStatus.BAD_REQUEST

        # Получаем роль "jury"
        jury_role = Role.query.filter_by(role_name="jury").first()
        if not jury_role:
            return {"message": "Роль 'jury' не найдена."}, HTTPStatus.NOT_FOUND

        # Изменяем роль пользователя на "jury"
        user.system_role = jury_role
        db.session.commit()

        return {"message": "Пользователь успешно добавлен в жюри."}, HTTPStatus.OK


@admin_ns.route('/organizers')
class OrganizerList(Resource):
    @jwt_required()
    @admin_ns.doc(description="Получение списка всех организаторов")
    def get(self):
        """Получить список всех организаторов"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        # Получаем роль "organizer"
        organizer_role = Role.query.filter_by(role_name="organizer").first()
        if not organizer_role:
            return {"message": "Роль 'organizer' не найдена."}, HTTPStatus.NOT_FOUND

        # Получаем всех пользователей с этой ролью
        organizers = User.query.filter_by(system_role_id=organizer_role.role_id).all()
        organizer_list = [user.to_dict() for user in organizers]
        return {"organizers": organizer_list}, HTTPStatus.OK

    @jwt_required()
    @admin_ns.expect(user_model)
    @admin_ns.doc(description="Добавление организатора")
    def post(self):
        """Добавить нового организатора"""
        if not admin_required():
            return {"message": "Доступ запрещён"}, HTTPStatus.FORBIDDEN

        data = request.get_json()
        user = get_user_by_username(data.get('username'))
        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        if user.system_role.role_name == "organizer":
            return {"message": "Пользователь уже является организатором."}, HTTPStatus.BAD_REQUEST

        # Получаем роль "organizer"
        organizer_role = Role.query.filter_by(role_name="organizer").first()
        if not organizer_role:
            return {"message": "Роль 'organizer' не найдена."}, HTTPStatus.NOT_FOUND

        # Изменяем роль пользователя на "organizer"
        user.system_role = organizer_role
        db.session.commit()
        return {"message": "Пользователь успешно добавлен в организаторы."}, HTTPStatus.OK
