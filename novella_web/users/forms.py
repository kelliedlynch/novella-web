from wtforms import Form, Field, StringField, PasswordField, BooleanField, validators
from flask import Markup
from wtforms.widgets import html_params


class ButtonWidget(object):
    html_params = staticmethod(html_params)

    def __init__(self, input_type='submit', text=''):
        self.input_type = input_type
        self.text = text

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        return Markup('<button type="submit" %s>%s</button>' % (self.html_params(name=field.name, **kwargs), field.text))


class ButtonField(Field):
  widget = ButtonWidget()

  def __init__(self, label=None, validators=None, text='Save', **kwargs):
    super(ButtonField, self).__init__(label, validators, **kwargs)
    self.text = text

  def _value(self):
        if self.data:
            return u''.join(self.data)
        else:
            return u''

class LoginForm(Form):
    email = StringField(description={'placeholder': 'Email Address'},
                        validators=[validators.Email(message='Please enter a valid email address.'),
                                    validators.Required(message='Please enter your email address.')])
    password = PasswordField(description={'placeholder': 'Password'},
                             validators=[validators.Length(min=6, max=16, message='Password is incorrect.'),
                                         validators.Required(message='Please enter your password.')])
    remember_me = BooleanField()
    submit = ButtonField(text='Log In')


class RegisterForm(Form):
    email = StringField(description={'placeholder': 'Email Address'},
                        validators=[validators.Email(message='Please enter a valid email address.'),
                                    validators.Required(message='Email address is required.')])
    password = PasswordField(description={'placeholder': 'Password'}, validators=[validators.Length(min=6,
                             max=32, message='Password must be between 6 and 32 characters.'),
                             validators.Required(message='Password is required.')])
    confirm_password = PasswordField(description={'placeholder': 'Confirm Password'},
                                     validators=[validators.EqualTo('password', message='Passwords do not match.'),
                                                 validators.Required(message='Please confirm your password')])
    submit = ButtonField(text='Register')