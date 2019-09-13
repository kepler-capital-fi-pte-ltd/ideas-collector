from flask import Flask

from .config import app_config
from .models import db
from .views.IdeaView import idea_api


def create_app(env_name: str):
    """

    Init application

    :param env_name: Name of the environment
    :return: Flask app
    """

    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    app.register_blueprint(idea_api, url_prefix='/api/v1/ideas')
    db.init_app(app)

    return app
