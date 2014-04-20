from flask import Flask

from novella_web.home import home

__all__ = ['create_app']

DEFAULT_APP_NAME = 'novella-web'

DEFAULT_BLUEPRINTS = (
    (home, '/'),
)

def create_app():

    blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__)

    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app, blueprints)
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
    pass
    # mail.init_app(app)
    # db.init_app(app)
    # oid.init_app(app)
    # cache.init_app(app)
    #
    # setup_themes(app)