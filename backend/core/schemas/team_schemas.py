from flask_restx import fields

from backend.core import api

team_model = api.model('Team', {
    'team_name': fields.String(required=True, description='Название команды'),
    'description': fields.String(required=False, description='Описание команды'),
})

team_invite_model = api.model('TeamInvite', {
    'team_name': fields.String(required=True, description='Название команды'),
    'username': fields.String(required=True, description='Имя пользователя для приглашения'),
})

team_artifacts = api.model("TeamArtifacts", {
    "github_url": fields.String(),
    "figma_url": fields.String(),
    "hosting_url": fields.String(),
    "presentation_url": fields.String(),
    "extra_links": fields.String()
})