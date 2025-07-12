from flask import Blueprint, render_template

bp = Blueprint('cuantica', __name__, url_prefix='/cuantica')

@bp.route('/')
def index():
    return render_template('cuantica/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('cuantica/demostracion.html')