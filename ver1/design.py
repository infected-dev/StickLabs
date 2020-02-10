from flask import Blueprint, render_template, request, redirect, url_for

from . import db
from .models import DesignMast

design = Blueprint('design', __name__)

x = DesignMast()


@design.route('/designMast')
def design_main():
    d_many = DesignMast.query.all()
    return render_template('Design/design.html', d_many=d_many)


@design.route('/addNewDesign', methods=['POST'])
def design_new():
    if request.form:
        d_no = request.form['d_no']
        name_d = request.form['d_name']
        design_x = DesignMast(design_code=d_no, design_name=name_d)
        design_x.update_data()
        db.session.add(design_x)
        db.session.commit()
        d_date = design_x.date_created
        d_user = design_x.changed_user_id
        data_dict = {'d_no': d_no, 'd_name': name_d, 'd_date': d_date, 'd_user': d_user}
        return data_dict

@design.route('/deleteDesigns', methods=['POST'])
def design_delete():
    if request.form:
        d_id = request.form.get('d_id')
        dx = DesignMast.query.get(int(d_id))
        db.session.delete(dx)
        db.session.commit()
        return redirect('/designMast')

@design.route('/changeData', methods=['POST'])
def design_change_data():
    if request.form:
        d_id = request.form.get('d_id')
        d_name = request.form.get('d_name')
        d = DesignMast.query.get(int(d_id))
        d.design_name = d_name
        d.update_date()
        db.session.commit()
        return redirect('/designMast')
        

@design.route('/designPrint', methods=['GET', 'POST'])
def design_print():
    d1 = DesignMast()
    d1 = d1.get_all() 
    if request.method == 'POST':
        if request.form:    
            d_id = request.form.get('d_id')
            print(d_id)
            return redirect(url_for('design.design_to_paper', d_id=d_id))
    return render_template('Design/print.html', d_many=d1)


@design.route('/paperPrint/<d_id>')
def design_to_paper(d_id):
    d = DesignMast.query.get(d_id)
    return render_template('Design/print_layout.html', d=d)
