from flask import Blueprint, render_template

bp = Blueprint('firma', __name__, url_prefix='/firma')

@bp.route('/')
def index():
    return render_template('firma/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('firma/demostracion.html')
