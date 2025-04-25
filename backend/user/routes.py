from flask import request
from flask_jwt_extended import jwt_required
from flask_restx import Resource

from backend.core.schemas.auth_schemas import login_model, user_model
from backend.core.services.profile_service import *
from . import user_ns
from ..core.models.hackathon_model import HackathonCase
from ..core.models.team_models import Team, TeamArtifacts, TeamCase
from ..core.schemas.team_schemas import team_invite_model, team_model, team_artifacts
from ..core.services.team_service import create_team, add_member_to_team


@user_ns.route('/register')
class UserRegister(Resource):
    @user_ns.expect(user_model)
    @user_ns.doc(description="Регистрация обычного пользователя (роль автоматически 'user')")
    def post(self):
        data = request.get_json()

        if "role_name" in data:
            del data["role_name"]

        data["role_name"] = "user"

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
class TeamCollection(Resource):
    @jwt_required()
    @user_ns.expect(team_model)
    @user_ns.doc(description="Создание новой команды")
    def post(self):
        data = request.get_json()
        username = get_jwt_identity()
        user = get_user_by_username(username)

        response = create_team({
            "team_name": data.get("team_name"),
            "description": data.get("description"),
            "team_lead_id": user.user_id,
        })

        return response


@user_ns.route('/teams/<string:team_name>')
class TeamItem(Resource):
    @jwt_required()
    @user_ns.doc(description="Получение участников команды")
    def get(self, team_name):
        team = Team.query.filter_by(team_name=team_name).first()
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND
        return [user.to_dict() for user in team.members], HTTPStatus.OK

    @jwt_required()
    @user_ns.expect(team_invite_model)
    @user_ns.doc(description="Приглашение пользователя в команду")
    def put(self, team_name):
        data = request.get_json()
        inviter = get_user_by_username(get_jwt_identity())
        print(inviter.user_id)

        team = Team.query.filter_by(team_name=team_name).first()
        print(team.team_lead_id)
        if not team or team.team_lead_id != inviter.user_id:
            return {"message": "Только тимлид может приглашать участников."}, HTTPStatus.FORBIDDEN

        invitee = User.query.filter_by(username=data.get("username")).first()
        if not invitee:
            return {"message": "Пользователь не найден."}, HTTPStatus.NOT_FOUND

        response, status = add_member_to_team(team.team_id, invitee.user_id)
        return response, status

    @jwt_required()
    @user_ns.doc(description="Выход пользователя из команды или удаление всей команды (если тимлид)")
    def delete(self, team_name):
        user = get_user_by_username(get_jwt_identity())
        team = Team.query.filter_by(team_name=team_name).first()
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        if team.team_lead_id == user.user_id:
            db.session.delete(team)
            db.session.commit()
            return {"message": f"Вы были тимлидом, команда '{team_name}' удалена."}, HTTPStatus.OK

        if user not in team.members:
            return {"message": "Вы не состоите в этой команде."}, HTTPStatus.BAD_REQUEST

        team.members.remove(user)
        db.session.commit()
        return {"message": f"Вы покинули команду '{team_name}'."}, HTTPStatus.OK


@user_ns.route('/teams/<string:team_name>/artifacts')
class TeamArtifactsResource(Resource):
    @jwt_required()
    @user_ns.doc(description="Получение артефактов команды")
    def get(self, team_name):
        team = Team.query.filter_by(team_name=team_name).first()
        if not team or not team.artifacts:
            return {"message": "Артефакты не найдены."}, HTTPStatus.NOT_FOUND

        return {
            "github_url": team.artifacts.github_url,
            "figma_url": team.artifacts.figma_url,
            "hosting_url": team.artifacts.hosting_url,
            "presentation_url": team.artifacts.presentation_url,
            "extra_links": team.artifacts.extra_links
        }, HTTPStatus.OK

    @jwt_required()
    @user_ns.expect(team_artifacts)
    @user_ns.doc(description="Создание или обновление артефактов команды")
    def put(self, team_name):
        user = get_user_by_username(get_jwt_identity())
        team = Team.query.filter_by(team_name=team_name).first()

        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND
        if team.team_lead_id != user.user_id:
            return {"message": "Только тимлид может редактировать артефакты."}, HTTPStatus.FORBIDDEN

        data = request.get_json()

        if not team.artifacts:
            artifacts = TeamArtifacts(team_id=team.team_id)
            db.session.add(artifacts)
        else:
            artifacts = team.artifacts

        artifacts.github_url = data.get("github_url")
        artifacts.figma_url = data.get("figma_url")
        artifacts.hosting_url = data.get("hosting_url")
        artifacts.presentation_url = data.get("presentation_url")
        artifacts.extra_links = data.get("extra_links")

        db.session.commit()
        return {"message": "Артефакты успешно сохранены."}, HTTPStatus.OK


@user_ns.route('/my-teams')
class MyTeams(Resource):
    @jwt_required()
    @user_ns.doc(description="Получение списка команд, в которых состоит пользователь (лид или участник)")
    def get(self):
        user = get_user_by_username(get_jwt_identity())

        lead_teams = Team.query.filter_by(team_lead_id=user.user_id).all()
        member_teams = user.teams

        all_teams = {team.team_id: team for team in lead_teams + member_teams}.values()

        result = []
        for team in all_teams:
            team_data = team.to_dict()

            team_case = TeamCase.query.filter_by(team_id=team.team_id).first()
            if team_case:
                hackathon_case = HackathonCase.query.filter_by(case_id=team_case.case_id).first()
                if hackathon_case:
                    team_data["case"] = hackathon_case.to_dict()
                else:
                    team_data["case"] = None
            else:
                team_data["case"] = None

            result.append(team_data)

        return result, HTTPStatus.OK
