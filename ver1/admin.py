from flask import Blueprint, render_template, request, url_for, redirect, flash

from .models import *

from flask_login import login_required, logout_user, current_user, login_user

admin = Blueprint('admin', __name__)

@admin.route('/')
def login():
    return render_template('Admin/signin.html')

@admin.route('/admin/')
def main_admin():
    roles = Role.query.all()
    users= User.query.all()
    designs= DesignMast.query.all()
    return render_template('Admin/admin.html', roles=roles, users=users, designs=designs)


@admin.route('/admin/adduser', methods=['POST'])
def add_user():
    if request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        role_id = request.form.get('roleid')
        plant_id = request.form.get('plantid')
    user = User(username=username, password=password, role_id=role_id, plant_id=plant_id)
    db.session.add(user)
    db.session.commit()
    return redirect('/admin')

@admin.route('/admin/addrole', methods=['POST'])
def add_role():
    if request.form:
        rolename = request.form.get('rolename')
        role = Role(role_name=rolename)
        db.session.add(role)
        db.session.commit()
        print(role)
    return redirect('/admin')



@admin.route('/admin/delete', methods=['POST'])
def delete_entity():
    if request.form:
        opp_id = int(request.form.get('opp_id'))
        if opp_id == 1: 
            user_id = request.form.get('userid')
            user = User.query.get(int(user_id))
            db.session.delete(user)
            db.session.commit()
        elif opp_id == 2:
            role_id = request.form.get('roleid')
            role = Role.query.get(int(role_id))
            db.session.delete(role)
            db.session.commit()
    return redirect('/admin')