from email.policy import default
from flask_login import UserMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass
from datetime import datetime

class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(64), unique=True)
    email           = db.Column(db.String(64), unique=True)
    password        = db.Column(db.LargeBinary)
    ip_address      = db.Column(db.String(100), nullable = True)
    user_agent      = db.Column(db.String(200), nullable = True)
    all_teams       = db.relationship('Teams', backref='teams', lazy=True)
    date_created    = db.Column(db.DateTime, nullable = False, default=datetime.now())

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username)

class Teams(db.Model):

    __tablename__ = 'Teams'

    id              = db.Column(db.Integer, primary_key=True)
    name            = db.Column(db.String(64), unique=True)
    color           = db.Column(db.String(64))
    user_id         = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    flag            = db.Column(db.String(1000), default='media/flags/')
    ip_address      = db.Column(db.String(100), nullable = True)
    user_agent      = db.Column(db.String(200), nullable = True)
    date_created    = db.Column(db.DateTime, nullable = False, default=datetime.now())

    def __repr__(self):
        return str(self.name)

@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username    = request.form.get('username')
    user        = Users.query.filter_by(username=username).first()
    return user if user else None
