import flask
from flask import current_app

main = flask.Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def index():
    return flask.render_template('home.html')