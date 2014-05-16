import flask
from extensions import db
from flask import current_app

home = flask.Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def index():
    with current_app.app_context():
        db.create_all()
    return flask.render_template('home.html')