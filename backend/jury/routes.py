from flask import request
from flask_jwt_extended import jwt_required, get_jwt
from flask_restx import Resource

from backend.core.schemas.auth_schemas import *
from backend.core.services.profile_service import *
from . import jury_ns
from ..core.models.hackathon_model import HackathonCase
from ..core.models.team_models import TeamArtifacts, Team, ArtifactReview, TeamCase, TeamMember
from ..core.schemas.hackathon_schemas import artifact_review_model


def resident_required():
    claims = get_jwt()
    if claims.get("role") != "jury":
        return False
    return True


@jury_ns.route('/login')
class ResidentLogin(Resource):
    @jury_ns.expect(login_model)
    @jury_ns.doc(description="Аутентификация резидента для получения токена доступа")
    def post(self):
        data = request.get_json()
        token = login_user("jury", data)
        if token:
            return {"access_token": token}, HTTPStatus.OK
        return {"message": AuthMessages.AUTH_INVALID_CREDENTIALS}, HTTPStatus.UNAUTHORIZED


@jury_ns.route('/profile')
class ResidentProfile(Resource):
    @jwt_required()
    @jury_ns.doc(description="Получение информации о резиденте")
    def get(self):
        if not resident_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN
        user, error, status = get_profile()
        if error:
            return error, status
        return get_user_info_response(user)

    @jwt_required()
    @jury_ns.expect(change_password_model)
    @jury_ns.doc(description="Изменение пароля резидента")
    def put(self):
        if not resident_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN
        data = request.get_json()
        return change_profile_password(data)

    @jwt_required()
    @jury_ns.doc(description="Удаление аккаунта резидента")
    def delete(self):
        if not resident_required():
            return {"message": AuthMessages.AUTH_ACCESS_DENIED}, HTTPStatus.FORBIDDEN
        return delete_profile()

@jury_ns.route('/teams/<string:team_name>/artifacts')
class TeamArtifactsResource(Resource):
    @jwt_required()
    @jury_ns.doc(description="Получение артефактов команды по названию с составом и кейсами")
    def get(self, team_name):
        if not resident_required():
            return {"message": "Доступ только для жюри."}, HTTPStatus.FORBIDDEN

        team = Team.query.filter_by(team_name=team_name).first()
        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        artifacts = TeamArtifacts.query.filter_by(team_id=team.team_id).first()
        if not artifacts:
            return {"message": "Артефакты для этой команды не найдены."}, HTTPStatus.NOT_FOUND

        team_members = TeamMember.query.filter_by(team_id=team.team_id).all()
        members_info = []
        for member in team_members:
            user = User.query.filter_by(user_id=member.user_id).first()
            if user:
                members_info.append(user.to_dict())

        team_case = TeamCase.query.filter_by(team_id=team.team_id).first()
        if not team_case:
            return {"message": "Кейс для этой команды не найден."}, HTTPStatus.NOT_FOUND

        case = HackathonCase.query.filter_by(case_id=team_case.case_id).first()
        if not case:
            return {"message": "Кейс не найден."}, HTTPStatus.NOT_FOUND

        response_data = {
            "artifacts": artifacts.to_dict(),  # метод должен быть реализован в модели TeamArtifacts
            "team_members": members_info,
            "case": case.to_dict()
        }

        return response_data, HTTPStatus.OK



@jury_ns.route('/teams/<int:team_id>/artifacts/review')
class ArtifactReviewResource(Resource):
    @jwt_required()
    @jury_ns.expect(artifact_review_model)
    @jury_ns.doc(description="Оценка артефактов команды жюри")
    def post(self, team_id):
        # Проверка, что пользователь имеет роль 'jury'
        if not resident_required():
            return {"message": "Доступ только для жюри."}, HTTPStatus.FORBIDDEN

        # Получаем пользователя (жюри) из токена
        jury_id = get_jwt_identity()
        team = Team.query.filter_by(team_id=team_id).first()

        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        # Проверяем, есть ли уже оценка для этой команды от данного жюри
        existing_review = ArtifactReview.query.filter_by(jury_id=jury_id, team_id=team_id).first()
        if existing_review:
            return {"message": "Вы уже оценивали этот артефакт."}, HTTPStatus.BAD_REQUEST

        # Создаем новую оценку
        data = request.get_json()
        review = ArtifactReview(
            jury_id=jury_id,
            team_id=team_id,
            criterion_1=data['criterion_1'],
            criterion_2=data['criterion_2'],
            criterion_3=data['criterion_3'],
            criterion_4=data['criterion_4'],
            criterion_5=data['criterion_5'],
            comment=data.get('comment', '')
        )

        db.session.add(review)
        db.session.commit()

        return {"message": "Оценка успешно добавлена."}, HTTPStatus.CREATED


@jury_ns.route('/teams/review/<string:team_name>')
class ArtifactReviewResource(Resource):
    @jwt_required()
    @jury_ns.expect(artifact_review_model)
    @jury_ns.doc(description="Оценка артефактов команды жюри по названию команды")
    def post(self, team_name):
        # Проверка, что пользователь имеет роль 'jury'
        if not resident_required():
            return {"message": "Доступ только для жюри."}, HTTPStatus.FORBIDDEN

        # Получаем пользователя (жюри) из токена
        jury_id = get_jwt_identity()
        team = Team.query.filter_by(team_name=team_name).first()

        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        # Проверяем, есть ли уже оценка для этой команды от данного жюри
        existing_review = ArtifactReview.query.filter_by(jury_id=jury_id, team_id=team.team_id).first()
        if existing_review:
            return {"message": "Вы уже оценивали этот артефакт."}, HTTPStatus.BAD_REQUEST

        # Создаем новую оценку
        data = request.get_json()
        review = ArtifactReview(
            jury_id=jury_id,
            team_id=team.team_id,
            criterion_1=data['criterion_1'],
            criterion_2=data['criterion_2'],
            criterion_3=data['criterion_3'],
            criterion_4=data['criterion_4'],
            criterion_5=data['criterion_5'],
            comment=data.get('comment', '')
        )

        db.session.add(review)
        db.session.commit()

        return {"message": "Оценка успешно добавлена."}, HTTPStatus.CREATED

    @jwt_required()
    @jury_ns.expect(artifact_review_model)
    @jury_ns.doc(description="Обновление оценки артефактов команды жюри по названию команды")
    def put(self, team_name):
        # Проверка, что пользователь имеет роль 'jury'
        if not resident_required():
            return {"message": "Доступ только для жюри."}, HTTPStatus.FORBIDDEN

        # Получаем пользователя (жюри) из токена
        jury_id = get_jwt_identity()
        team = Team.query.filter_by(team_name=team_name).first()

        if not team:
            return {"message": "Команда не найдена."}, HTTPStatus.NOT_FOUND

        # Проверяем, есть ли оценка для этой команды от данного жюри
        review = ArtifactReview.query.filter_by(jury_id=jury_id, team_id=team.team_id).first()
        if not review:
            return {"message": "Вы еще не оценивали этот артефакт."}, HTTPStatus.BAD_REQUEST

        # Обновляем оценку
        data = request.get_json()
        review.criterion_1 = data['criterion_1']
        review.criterion_2 = data['criterion_2']
        review.criterion_3 = data['criterion_3']
        review.criterion_4 = data['criterion_4']
        review.criterion_5 = data['criterion_5']
        review.comment = data.get('comment', review.comment)

        db.session.commit()

        return {"message": "Оценка успешно обновлена."}, HTTPStatus.OK


@jury_ns.route('/teams/review-pending')
class PendingArtifactReviewResource(Resource):
    @jwt_required()
    @jury_ns.doc(description="Получить список команд, которые нужно оценить")
    def get(self):
        jury_id = get_jwt_identity()

        pending_teams = Team.query.filter(
            Team.artifacts != None,  # Проверяем, что команда отправила артефакты
            ~Team.artifact_reviews.any(ArtifactReview.jury_id == jury_id)  # И ещё не оценены этим жюри
        ).all()

        if not pending_teams:
            return {"message": "Нет команд для оценки."}, HTTPStatus.NOT_FOUND

        # Сериализация данных с использованием метода to_dict()
        teams_data = [team.to_dict() for team in pending_teams]

        return {"teams": teams_data}, HTTPStatus.OK


@jury_ns.route('/teams/reviewed')
class ReviewedArtifactReviewResource(Resource):
    @jwt_required()
    @jury_ns.doc(description="Получить список команд, которые уже оценены")
    def get(self):
        jury_id = get_jwt_identity()
        reviewed_teams = Team.query.filter(
            Team.artifacts != None,  # Проверяем, что команда отправила артефакты
            Team.artifact_reviews.any(ArtifactReview.jury_id == jury_id)  # И оценены этим жюри
        ).all()

        if not reviewed_teams:
            return {"message": "Нет оцененных команд."}, HTTPStatus.NOT_FOUND

        teams_data = [team.to_dict() for team in reviewed_teams]

        return {"teams": teams_data}, HTTPStatus.OK
