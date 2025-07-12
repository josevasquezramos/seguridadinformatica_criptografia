from flask import Blueprint, render_template, request, jsonify
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
import base64

bp = Blueprint('firma', __name__, url_prefix='/firma')

# Generamos un par de claves para la demostración (en producción esto sería por usuario)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

@bp.route('/')
def index():
    return render_template('firma/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('firma/demostracion.html')

@bp.route('/generar-firma', methods=['POST'])
def generar_firma():
    data = request.get_json()
    documento = data['documento'].encode('utf-8')
    
    # Generar hash del documento
    digest = hashes.Hash(hashes.SHA256())
    digest.update(documento)
    hash_documento = digest.finalize()
    
    # Firmar el hash
    firma = private_key.sign(
        hash_documento,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    # Serializar clave pública
    pub_key_pem = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    return jsonify({
        'hash': base64.b64encode(hash_documento).decode('utf-8'),
        'firma': base64.b64encode(firma).decode('utf-8'),
        'clave_publica': pub_key_pem
    })

@bp.route('/verificar-firma', methods=['POST'])
def verificar_firma():
    data = request.get_json()
    
    try:
        # Decodificar datos
        documento = data['documento'].encode('utf-8')
        firma = base64.b64decode(data['firma'])
        pub_key_pem = data['clave_publica'].encode('utf-8')
        
        # Reconstruir clave pública (en producción se validaría el certificado)
        from cryptography.hazmat.primitives.serialization import load_pem_public_key
        public_key_verif = load_pem_public_key(pub_key_pem)
        
        # Generar hash del documento recibido
        digest = hashes.Hash(hashes.SHA256())
        digest.update(documento)
        hash_documento = digest.finalize()
        
        # Verificar firma
        public_key_verif.verify(
            firma,
            hash_documento,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        
        return jsonify({
            'valido': True,
            'documento_original': documento.decode('utf-8')
        })
        
    except Exception as e:
        return jsonify({
            'valido': False,
            'error': str(e)
        }), 400