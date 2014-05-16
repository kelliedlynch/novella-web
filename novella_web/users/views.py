from flask import Blueprint
from flask import request, render_template

from forms import LoginForm


users = Blueprint('user', __name__, template_folder='templates', url_prefix='/users')


@users.route('../login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        pass
    elif request.method == 'POST':
        pass
    else:
        return render_template('login.html', login_form=login_form)