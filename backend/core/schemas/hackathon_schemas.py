from flask_restx import fields

from backend.core import api

hackathon_case_model = api.model('HackathonCase', {
    'title': fields.String(required=True, description="Название кейса хакатона"),
    'description': fields.String(required=True, description="Описание кейса хакатона"),
    'file': fields.String(description="Загрузите файл с подробным ТЗ (PDF или DOCX)", required=True),
})
artifact_review_model = api.model('ArtifactReview', {
    'criterion_1': fields.Integer(required=True, min=1, max=10, description="Критерий 1"),
    'criterion_2': fields.Integer(required=True, min=1, max=10, description="Критерий 2"),
    'criterion_3': fields.Integer(required=True, min=1, max=10, description="Критерий 3"),
    'criterion_4': fields.Integer(required=True, min=1, max=10, description="Критерий 4"),
    'criterion_5': fields.Integer(required=True, min=1, max=10, description="Критерий 5"),
    'comment': fields.String(required=False, description="Комментарий к оценке")
})
