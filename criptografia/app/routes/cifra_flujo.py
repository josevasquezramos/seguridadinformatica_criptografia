from flask import Blueprint, render_template

bp = Blueprint('cifra_flujo', __name__, url_prefix='/cifra-flujo')

@bp.route('/')
def index():
    return render_template('cifra_flujo/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('cifra_flujo/demostracion.html')
