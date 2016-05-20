from flask.ext.wtf import form
from wtforms import Stringfield, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form)
    openid = StringField('openid',validators=[DataRequired()])
    remember_me = BooleanField('remember_me',default=Flase)
