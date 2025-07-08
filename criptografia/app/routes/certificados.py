from flask import Blueprint, render_template

bp = Blueprint('certificados', __name__, url_prefix='/certificados')

@bp.route('/')
def index():
    return render_template('certificados/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('certificados/demostracion.html')
