from flask import Blueprint, render_template, request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import base64

bp = Blueprint('simetrico_bloque', __name__, url_prefix='/simetrico-bloque')

def cifrar_aes(texto_plano, clave):
    backend = default_backend()
    clave_bytes = clave.encode('utf-8')
    clave_bytes = clave_bytes[:32].ljust(32, b'\0')  # AES-256 requiere 32 bytes

    iv = os.urandom(16)  # vector de inicialización aleatorio
    cipher = Cipher(algorithms.AES(clave_bytes), modes.CBC(iv), backend=backend)

    padder = padding.PKCS7(128).padder()
    texto_padded = padder.update(texto_plano.encode()) + padder.finalize()

    cifrador = cipher.encryptor()
    texto_cifrado = cifrador.update(texto_padded) + cifrador.finalize()

    # Devolver en base64 para mostrarlo como texto legible
    return base64.b64encode(iv + texto_cifrado).decode()

def descifrar_aes(texto_cifrado_b64, clave):
    backend = default_backend()
    clave_bytes = clave.encode('utf-8')
    clave_bytes = clave_bytes[:32].ljust(32, b'\0')

    datos = base64.b64decode(texto_cifrado_b64)
    iv = datos[:16]
    texto_cifrado = datos[16:]

    cipher = Cipher(algorithms.AES(clave_bytes), modes.CBC(iv), backend=backend)

    descifrador = cipher.decryptor()
    texto_padded = descifrador.update(texto_cifrado) + descifrador.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    texto_plano = unpadder.update(texto_padded) + unpadder.finalize()

    return texto_plano.decode('utf-8', errors='ignore')

@bp.route('/')
def index():
    return render_template('simetrico_bloque/index.html')

@bp.route('/demostracion', methods=['GET', 'POST'])
def demostracion():
    resultado = None
    modo = None
    texto_original = ""
    clave = ""

    if request.method == 'POST':
        texto_original = request.form['texto']
        clave = request.form['clave']
        modo = request.form['modo']

        if modo == 'cifrar':
            resultado = cifrar_aes(texto_original, clave)
        elif modo == 'descifrar':
            try:
                resultado = descifrar_aes(texto_original, clave)
            except Exception as e:
                resultado = f"Error al descifrar: {str(e)}"

    return render_template('simetrico_bloque/demostracion.html',
                           resultado=resultado,
                           texto_original=texto_original,
                           clave=clave,
                           modo=modo)
