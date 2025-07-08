from flask import Blueprint, render_template

bp = Blueprint('mochila', __name__, url_prefix='/mochila')

@bp.route('/')
def index():
    return render_template('mochila/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('mochila/demostracion.html')
