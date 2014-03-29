from flask import Blueprint

# from novella_web import app

home = Blueprint('home', __name__, template_folder='templates')

@home.route('/')
def index():
    return 'Hello, world!'