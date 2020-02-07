from flask import Blueprint, render_template, request, url_for
from . import db
from .models import DesignMast

design = Blueprint('design', __name__)

@design.route('/designmast')
def design_main():
    return render_template('Design/design.html')


@design.route('/addNewDesign', methods=['POST'])
def design_new():
    if request.form:
        d_no = request.form['d_no']
        name_d = request.form['d_name']
        design = DesignMast(design_code=d_no, design_name=name_d)
        design.updateData()
        db.session.add(design)
        db.session.commit()
        return {'d_no': d_no, 'd_name':name_d}

