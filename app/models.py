from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Radio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serial_number = db.Column(db.String(50), nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    model_id = db.Column(db.String(100), nullable=False)
    is_issued = db.Column(db.Boolean, default=False)
    issued_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    issued_at = db.Column(db.DateTime, default=db.func.now())
    returned_at = db.Column(db.DateTime, nullable=True)
