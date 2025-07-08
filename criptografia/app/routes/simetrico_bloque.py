from flask import Blueprint, render_template

bp = Blueprint('simetrico_bloque', __name__, url_prefix='/simetrico-bloque')

@bp.route('/')
def index():
    return render_template('simetrico_bloque/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('simetrico_bloque/demostracion.html')
