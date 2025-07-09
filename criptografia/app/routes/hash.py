from flask import Blueprint, render_template, request
import hashlib

bp = Blueprint('hash', __name__, url_prefix='/hash')

@bp.route('/')
def index():
    return render_template('hash/index.html')

@bp.route('/demostracion', methods=['GET', 'POST'])
def demostracion():
    resultado = None
    texto = ''
    algoritmo = ''
    hash_generado = ''
    explicacion = ''
    intermedios = []

    algoritmos_disponibles = {
        'md5': 'MD5 genera un hash de 128 bits. Es rápido pero vulnerable a colisiones. Se usa aún en comprobaciones simples de integridad.',
        'sha1': 'SHA-1 genera un hash de 160 bits. Fue ampliamente usado, pero ya no es seguro contra colisiones.',
        'sha256': 'SHA-256 genera un hash de 256 bits. Seguro, robusto y usado en criptografía moderna y blockchain.',
        'sha512': 'SHA-512 genera un hash de 512 bits. Muy seguro, útil para ambientes donde se requiere mayor robustez.'
    }

    if request.method == 'POST':
        texto = request.form.get('texto', '')
        algoritmo = request.form.get('algoritmo', '')

        if texto and algoritmo in algoritmos_disponibles:
            encoded = texto.encode()
            if algoritmo == 'md5':
                hash_obj = hashlib.md5()
            elif algoritmo == 'sha1':
                hash_obj = hashlib.sha1()
            elif algoritmo == 'sha256':
                hash_obj = hashlib.sha256()
            elif algoritmo == 'sha512':
                hash_obj = hashlib.sha512()

            # Simular bloques de escritura en pasos
            for i in range(0, len(encoded), 8):
                parte = encoded[i:i+8]
                hash_obj.update(parte)
                intermedios.append({
                    'bloque': parte.hex(),
                    'contenido': parte.decode(errors='ignore'),
                    'digest_parcial': hash_obj.hexdigest()
                })

            hash_generado = hash_obj.hexdigest()

            resultado = {
                'texto': texto,
                'algoritmo': algoritmo.upper(),
                'hash': hash_generado,
                'explicacion': algoritmos_disponibles[algoritmo],
                'pasos': intermedios
            }

    return render_template('hash/demostracion.html', resultado=resultado)
