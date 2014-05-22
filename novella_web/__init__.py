from importlib import import_module

from flask import Flask, g
from flask_login import LoginManager

from extensions import db
from users import User

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
    app.secret_key = app.config['APP_SECRET_KEY']


def configure_blueprints(app):
    for blueprint_name in app.config['DEFAULT_BLUEPRINTS']:
        try:
            package_path = __name__
            if blueprint_name != 'main':
                package_path = package_path + '.' + blueprint_name
            blueprint = import_module('.views', package=package_path)
            app.register_blueprint(getattr(blueprint, blueprint_name))
        except:
            print "Error registering blueprint:", blueprint_name


def configure_before_handlers(app):
    pass
    # @app.before_request
    # def authenticate():
    #     g.user = getattr(g.identity, 'user', None)


def configure_extensions(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(userid):
        return User.get(userid)

    db.init_app(app)

app = create_app()