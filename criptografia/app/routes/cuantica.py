from flask import Blueprint, render_template

bp = Blueprint('cuantica', __name__, url_prefix='/cuantica')

# Ruta principal para Criptografía Cuántica
@bp.route('/')
def index():
    return render_template('cuantica/index.html')

# Ruta para la demostración de Criptografía Cuántica
@bp.route('/demostracion')
def demostracion():
    return render_template('cuantica/demostracion.html')
