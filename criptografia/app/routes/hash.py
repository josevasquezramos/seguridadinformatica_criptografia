from flask import Blueprint, render_template

bp = Blueprint('hash', __name__, url_prefix='/hash')

@bp.route('/')
def index():
    return render_template('hash/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('hash/demostracion.html')
