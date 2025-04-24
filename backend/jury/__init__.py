from flask_restx import Namespace

jury_ns = Namespace('jury', description='Эндпоинты для резидента')

from . import routes
