from flask import Blueprint, render_template, request, url_for
from . import db

admin = Blueprint('admin', __name__)

@admin.route('/')
def main_admin():
    return render_template('Admin/admin.html')
