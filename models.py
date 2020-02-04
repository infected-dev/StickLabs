from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from . import db

class User(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey='role.role_id')
    plant_id = db.Column(db.Integer, db.ForeignKey = 'plant.plant_id')

    def __init__(self, username, password, role_id, plant_id):
        self.username = username
        self.password = password
        self.role_id = role_id
        self.plant_id = plant_id
    
    def get_role(self):
        return self.role_id

class Role(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'role'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(20))
    users = db.relationship('User', backref='roles')

    def __init__(self, role_name):
        self.role_name = role_name

class DesignMast(db.Model):
    __tablename__ = 'designmast'

    design_code = db.Column(db.Integer, primary_key=True)
    design_name = db.Column(db.String(50))
    changed_user_id = db.Column(db.Integer, db.ForeignKey='user.user_id')
    date_created = db.Column(db.Date)
    date_changed = db.Column(db.Date)

    def __init__(self, design_code, design_name, changed_user_id, date_created, date_changed):
        self.design_code = design_code
        self.design_name = design_name
        self.changed_user_id = changed_user_id
        self.date_created = datetime.now().date()
        self.date_changed = date_changed

    