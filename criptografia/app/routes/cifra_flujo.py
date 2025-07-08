from flask import Blueprint, render_template, request

bp = Blueprint('cifra_flujo', __name__, url_prefix='/cifra-flujo')

def xor_cipher(data, clave):
    if isinstance(data, str):
        data = data.encode()
    clave_repetida = (clave * (len(data) // len(clave) + 1)).encode()
    resultado = bytes([b ^ k for b, k in zip(data, clave_repetida)])
    return resultado


@bp.route('/')
def index():
    return render_template('cifra_flujo/index.html')


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
            cifrado = xor_cipher(texto_original, clave)
            resultado = cifrado.hex()  # Se muestra en hexadecimal
        elif modo == 'descifrar':
            try:
                cifrado_bytes = bytes.fromhex(texto_original)
                clave_repetida = (clave * (len(cifrado_bytes) // len(clave) + 1)).encode()
                descifrado = bytes([b ^ k for b, k in zip(cifrado_bytes, clave_repetida)])
                resultado = descifrado.decode('utf-8', errors='ignore')
            except Exception as e:
                resultado = f"Error al descifrar: {str(e)}"

    return render_template('cifra_flujo/demostracion.html',
                           resultado=resultado,
                           texto_original=texto_original,
                           clave=clave,
                           modo=modo)
