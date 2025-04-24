from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from backend.core.schemas.auth_schemas import login_model, user_model
from backend.core.services.profile_service import *
from . import user_ns
from ..core.models.team_models import Team
from ..core.schemas.team_schemas import team_invite_model, team_model
from ..core.services.team_service import create_team, add_member_to_team


@user_ns.route('/register')
class UserRegister(Resource):
    @user_ns.expect(user_model)
    @user_ns.doc(description="Регистрация обычного пользователя (роль автоматически 'user')")
    def post(self):
        data = request.get_json()
        return register_user(data)


@user_ns.route('/login')
class UserLogin(Resource):
    @user_ns.expect(login_model)
    @user_ns.doc(description="Аутентификация обычного пользователя для получения токена доступа")
    def post(self):
        data = request.get_json()
        token = login_user("user", data)
        if token:
            return {"access_token": token}, HTTPStatus.OK
        return {"message": AuthMessages.AUTH_INVALID_CREDENTIALS}, HTTPStatus.UNAUTHORIZED


@user_ns.route('/profile')
class UserProfile(Resource):
    @jwt_required()
    @user_ns.doc(description="Получение информации о пользователе")
    def get(self):
        user, error, status = get_profile()
        if error:
            return error, status
        return get_user_info_response(user)

    @jwt_required()
    @user_ns.expect(user_model)
    @user_ns.doc(description="Редактирование аккаунта пользователя")
    def put(self):
        data = request.get_json()
        username = get_jwt_identity()
        user = User.query.filter_by(username=username).first()

        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        response = update_user_profile(user, data)

        return response, HTTPStatus.OK

    @jwt_required()
    @user_ns.doc(description="Удаление аккаунта")
    def delete(self):
        return delete_profile()


@user_ns.route('/teams')
class TeamCreate(Resource):
    @jwt_required()
    @user_ns.expect(team_model)
    @user_ns.doc(description="Создание команды")
    def post(self):
        data = request.get_json()

        username = get_jwt_identity()
        user = get_user_by_username(username)

        # Внесли изменения: теперь команда создается по имени
        response = create_team({
            "team_name": data.get("team_name"),
            "description": data.get("description"),
            "team_lead_id": user.user_id,
        })

        return response


@user_ns.route('/teams/invite')
class TeamInvite(Resource):
    @jwt_required()
    @user_ns.expect(team_invite_model)
    @user_ns.doc(description="Приглашение пользователя в команду")
    def post(self):
        data = request.get_json()
        team_name = data.get("team_name")
        username = data.get("username")  # Поиск по имени пользователя

        current_username = get_jwt_identity()
        current_user = get_user_by_username(current_username)

        # Изменение поиска команды по имени
        team = Team.query.filter_by(team_name=team_name).first()

        if not team or team.team_lead_id != current_user.user_id:
            return {"message": "Только тимлид может пригласить участников."}, HTTPStatus.FORBIDDEN

        # Поиск пользователя по имени
        user = User.query.filter_by(username=username).first()
        if not user:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        response, status = add_member_to_team(team.team_id, user.user_id)
        return response, status


@user_ns.route('/teams/<string:team_name>/members')
class TeamMembers(Resource):
    @jwt_required()
    @user_ns.doc(description="Получение участников команды")
    def get(self, team_name):
        # Получаем команду по имени
        team = Team.query.filter_by(team_name=team_name).first()

        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        # Получаем участников команды
        members = team.members

        return [user.to_dict() for user in members], HTTPStatus.OK
