from flask import Blueprint, render_template

bp = Blueprint('blockchain', __name__, url_prefix='/blockchain')

@bp.route('/')
def index():
    return render_template('blockchain/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('blockchain/demostracion.html')
