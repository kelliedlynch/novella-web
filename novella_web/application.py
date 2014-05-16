from flask import Flask
from flask_login import LoginManager

from extensions import db

__all__ = ['create_app']

DEFAULT_APP_NAME = 'novella-web'


def create_app():

    app = Flask(__name__)

    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app)
    configure_before_handlers(app)

    return app


def configure_app(app):
    app.config.from_pyfile('config.py')
    app.config.from_envvar('APP_CONFIG', silent=True)


def configure_blueprints(app, blueprints):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)


def configure_before_handlers(app):
    pass
    # @app.before_request
    # def authenticate():
    #     g.user = getattr(g.identity, 'user', None)


def configure_extensions(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    # mail.init_app(app)
    db.init_app(app)
    # oid.init_app(app)
    # cache.init_app(app)
    #
    # setup_themes(app)