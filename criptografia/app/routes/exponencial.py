from flask import Blueprint, render_template, request
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import secrets
import base64

bp = Blueprint('exponencial', __name__, url_prefix='/exponencial')

@bp.route('/')
def index():
    return render_template('exponencial/index.html')

@bp.route('/demostracion', methods=['GET', 'POST'])
def demostracion():
    resultado = None
    if request.method == 'POST':
        try:
            modo = request.form['modo']

            # Valores públicos
            p = int(request.form['p'])
            g = int(request.form['g'])

            if modo == 'manual':
                a = int(request.form['a'])
                b = int(request.form['b'])
            else:
                a = secrets.randbelow(p - 2) + 2
                b = secrets.randbelow(p - 2) + 2

            A = pow(g, a, p)
            B = pow(g, b, p)

            # Clave compartida
            sA = pow(B, a, p)
            sB = pow(A, b, p)

            clave_secreta = sha256(str(sA).encode()).digest()

            mensaje = request.form.get('mensaje')
            mensaje_cifrado = mensaje_descifrado = None
            nonce = tag = ciphertext = None

            if mensaje:
                cipher = AES.new(clave_secreta, AES.MODE_GCM)
                nonce = cipher.nonce
                ciphertext, tag = cipher.encrypt_and_digest(mensaje.encode())
                mensaje_cifrado = base64.b64encode(nonce + tag + ciphertext).decode()

                # Simulamos que el receptor descifra con la misma clave
                cipher_dec = AES.new(clave_secreta, AES.MODE_GCM, nonce=nonce)
                mensaje_descifrado = cipher_dec.decrypt_and_verify(ciphertext, tag).decode()

            resultado = {
                'modo': modo,
                'p': p,
                'g': g,
                'a': a,
                'b': b,
                'A': A,
                'B': B,
                'sA': sA,
                'sB': sB,
                'clave_hex': clave_secreta.hex(),
                'mensaje': mensaje,
                'mensaje_cifrado': mensaje_cifrado,
                'mensaje_descifrado': mensaje_descifrado
            }

        except Exception as e:
            resultado = {'error': str(e)}

    return render_template('exponencial/demostracion.html', resultado=resultado)

