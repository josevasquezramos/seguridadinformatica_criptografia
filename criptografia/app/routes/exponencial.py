from flask import Blueprint, render_template

bp = Blueprint('exponencial', __name__, url_prefix='/exponencial')

@bp.route('/')
def index():
    return render_template('exponencial/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('exponencial/demostracion.html')
