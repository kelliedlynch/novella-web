from flask import Blueprint
from flask import request, render_template
from flask_login import login_user, current_user

from forms import LoginForm
from models import User


users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')


@users.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        login_user(current_user)
        return render_template('login.html', login_form=login_form)
    elif request.method == 'POST':
        return render_template('login.html', login_form=login_form)
    else:
        return render_template('login.html', login_form=login_form)