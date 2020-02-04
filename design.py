from flask import Blueprint, render_template, request, url_for
from . import db

design = Blueprint('design', __name__)

@design.route('/designmast')
def design_main():
    return render_template('Design/design.html')