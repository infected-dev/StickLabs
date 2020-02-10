from . import db
from datetime import datetime


class Plant(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'plant'

    plant_id = db.Column(db.Integer, primary_key=True)
    plant_name = db.Column(db.String(30))

    def __init__(self, plant_name):
        self.plant_name = plant_name


class User(db.Model):
    __bind_key__ = 'admin'
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'))
    plant_id = db.Column(db.Integer, db.ForeignKey('plant.plant_id'))

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
    changed_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    date_created = db.Column(db.Date)
    date_changed = db.Column(db.Date)

    def update_data(self):
        self.date_created = datetime.now().date()
        self.changed_user_id = 3
        db.session.add(self)
        db.session.commit()

    def get_all(self):
        x = self.query.all()
        return x

    def update_date(self):
        self.date_changed = datetime.now().date()
        db.session.commit()

        