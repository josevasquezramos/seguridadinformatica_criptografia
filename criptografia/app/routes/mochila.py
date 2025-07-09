from flask import Blueprint, render_template, request

bp = Blueprint('mochila', __name__, url_prefix='/mochila')

@bp.route('/')
def index():
    return render_template('mochila/index.html')

@bp.route('/demostracion', methods=['GET', 'POST'])
def demostracion():
    resultado = None
    if request.method == 'POST':
        accion = request.form.get('accion')

        if accion == 'cifrar':
            mensaje = request.form.get('mensaje', '')
            resultado = cifrar_mochila(mensaje)
            resultado['modo'] = 'cifrado'

        elif accion == 'descifrar':
            cifrado_input = request.form.get('cifrado', '')
            try:
                valores = [int(x.strip()) for x in cifrado_input.split(',')]
                resultado = descifrar_mochila(valores)
                resultado['modo'] = 'descifrado'
            except:
                resultado = {'error': 'Entrada no válida para descifrado.'}

    return render_template('mochila/demostracion.html', resultado=resultado)

# Función de cifrado
def cifrar_mochila(mensaje):
    mochila_privada = [2, 3, 7, 14, 30, 57, 120, 251]
    q = 491
    r = 41
    mochila_publica = [(r * w_i) % q for w_i in mochila_privada]

    binario = ''.join(format(ord(c), '08b') for c in mensaje)
    bloques = [binario[i:i+8] for i in range(0, len(binario), 8)]
    cifrado = [sum(int(b) * k for b, k in zip(bloque, mochila_publica)) for bloque in bloques]

    return {
        'mensaje_original': mensaje,
        'mensaje_binario': binario,
        'bloques': bloques,
        'mochila_publica': mochila_publica,
        'clave_privada': mochila_privada,
        'q': q,
        'r': r,
        'cifrado': cifrado
    }

# Función de descifrado
def descifrar_mochila(cifrado):
    mochila_privada = [2, 3, 7, 14, 30, 57, 120, 251]
    q = 491
    r = 41
    r_inv = modinv(r, q)

    descifrado_bin = []
    for c in cifrado:
        s = (c * r_inv) % q
        bloque = resolver_mochila(mochila_privada[::-1], s)
        bloque = bloque[::-1] if bloque else '00000000'
        descifrado_bin.append(bloque)

    binario_total = ''.join(descifrado_bin)
    texto = ''.join(chr(int(binario_total[i:i+8], 2)) for i in range(0, len(binario_total), 8))

    return {
        'clave_privada': mochila_privada,
        'q': q,
        'r': r,
        'r_inv': r_inv,
        'descifrado_bin': descifrado_bin,
        'mensaje_descifrado': texto,
        'cifrado': cifrado
    }


# Función auxiliar: inverso modular
def modinv(a, m):
    # Algoritmo extendido de Euclides
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Función auxiliar: resolver mochila superincreciente
def resolver_mochila(mochila_invertida, suma_objetivo):
    bits = []
    for peso in mochila_invertida:
        if peso <= suma_objetivo:
            bits.append('1')
            suma_objetivo -= peso
        else:
            bits.append('0')
    if suma_objetivo == 0:
        return ''.join(bits)
    else:
        return None
