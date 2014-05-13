import flask
from forms import LoginForm

home = flask.Blueprint('home', __name__, template_folder='templates')


@home.route('/')
def index():
    return flask.render_template('home.html')

@home.route('login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(flask.request.form)
    if flask.request.method == 'POST' and login_form.validate():
        pass
    elif flask.request.method == 'POST':
        pass
    else:
        return flask.render_template('login.html', login_form=login_form)