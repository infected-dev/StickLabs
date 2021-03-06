import os

from flask import Flask, render_template, redirect, url_for, Blueprint

from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager


basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()
login_manager = LoginManager()


app = Flask(__name__)


app.config['SECRET_KEY'] = 'stickerbanale'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_BINDS'] = {'admin' : 'sqlite:///db_admin.sqlite3'}
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


db.init_app(app)


login_manager.init_app(app)
login_manager.login_view = 'admin.login_main'
login_manager.login_message = "Please Sign In."


admin = Admin(app, name='DesingAdmin', template_mode='bootstrap3')


from .design import design as design_blueprint
app.register_blueprint(design_blueprint)
 

if __name__ == '__main__':
   app.run(debug=True)