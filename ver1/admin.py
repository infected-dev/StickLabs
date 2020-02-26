from flask import Blueprint, render_template, request, url_for, flash, redirect
from . import db
from .models import User, Role

admin = Blueprint('admin', __name__)

@admin.route('/')
def main_admin():
    roles = Role.query.all()
    print(roles)
    return render_template('Admin/admin.html', roles=roles)

@admin.route('/addNewUser')
def user_curd():
    users = User.query.all()
    user_names = [u.username for u in users]
    if request.form:
        operation_id = request.form.get('op_id')
        if operation_id == 1:
            username = request.form.get('username')
            if username in user_names:
                flash('User already Created')
                return redirect('admin.main_admin')
            else:    
                password = request.form.get('password')
                role_id = request.form.get('role_id')
                user_x = User(username=username, password=password, role_id=role_id)
                db.session.add(user_x)
                db.session.commit()
                flash('User Created and good for logging in.')
                return redirect(url_for('admin.main_admin'))

@admin.route('/addNewRole', methods=['POST'])
def role_curd():
    roles = Role.query.all()
    role_names = [r.role_name for r in roles]
    if request.form:
        operation_id = int(request.form.get('op_id'))
        print(operation_id)
        if operation_id == 1:
            role_name = request.form.get('role_name')
            role_name = role_name.upper()
            if role_name in role_names:
                flash('Role Already Exists')
                return redirect(url_for('admin.main_admin'))
            else:
                role_x = Role(role_name=role_name)
                db.session.add(role_x)
                db.session.commit()
                flash('Role Created, Can be used to Assign to users.')
                return redirect(url_for('admin.main_admin'))
        elif operation_id == 2:
            role_id = request.form.get('role_id')
            role_x = Role.query.get(role_id)
            db.session.delete(role_x)
            db.session.commit()
            flash('Role Successfully Deleted')
    return redirect(url_for('admin.main_admin'))
            


@admin.route('/login')
def login_main():
    return render_template('Admin/signin.html')