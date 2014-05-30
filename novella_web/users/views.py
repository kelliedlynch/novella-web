from flask import Blueprint
from flask import request, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user

from forms import LoginForm, RegisterForm
from models import User
from novella_web.extensions import db, bcrypt


users = Blueprint('users', __name__, template_folder='templates', url_prefix='/users')


@users.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        u = User.query.filter_by(email=request.form['email']).first()
        if bcrypt.check_password_hash(u.password, login_form.password.data):
            login_user(u)
            login_form = LoginForm()
        return render_template('login.html', login_form=login_form)
    elif request.method == 'POST':
        return render_template('login.html', login_form=login_form)
    else:
        return render_template('login.html', login_form=login_form)


@users.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('.login'))


@users.route('/register/', methods=['GET', 'POST'])
def register():

    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        new_user = User()
        register_form.populate_obj(new_user)
        new_user.password = bcrypt.generate_password_hash(new_user.password)
        db.session.add(new_user)
        db.session.commit()
        print 'successfully registered'
        return render_template('register.html', register_form=register_form)
    elif request.method == 'POST':
        return render_template('register.html', register_form=register_form)
    else:
        return render_template('register.html', register_form=register_form)