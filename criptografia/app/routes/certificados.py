from flask import Blueprint, render_template, request, jsonify
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.serialization import Encoding
import datetime
import base64

bp = Blueprint('certificados', __name__, url_prefix='/certificados')

# Generar clave privada para la CA de demostración
ca_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Crear certificado auto-firmado para la CA
ca_subject = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CA Demo"),
    x509.NameAttribute(NameOID.COMMON_NAME, "ca.demo.com"),
])

ca_cert = x509.CertificateBuilder().subject_name(
    ca_subject
).issuer_name(
    ca_subject
).public_key(
    ca_private_key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).add_extension(
    x509.BasicConstraints(ca=True, path_length=None),
    critical=True,
).sign(ca_private_key, hashes.SHA256())

@bp.route('/')
def index():
    return render_template('certificados/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('certificados/demostracion.html')

@bp.route('/generar-certificado', methods=['POST'])
def generar_certificado():
    data = request.get_json()
    common_name = data['common_name']
    
    # Generar clave para el certificado
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    
    # Crear solicitud
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "California"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Demo Org"),
        x509.NameAttribute(NameOID.COMMON_NAME, common_name),
    ])
    
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        ca_cert.subject
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        datetime.datetime.utcnow() + datetime.timedelta(days=90)
    ).add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True,
    ).sign(ca_private_key, hashes.SHA256())
    
    return jsonify({
        'certificado': cert.public_bytes(Encoding.PEM).decode('utf-8'),
        'clave_privada': private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8'),
        'certificado_ca': ca_cert.public_bytes(Encoding.PEM).decode('utf-8')
    })

@bp.route('/verificar-certificado', methods=['POST'])
def verificar_certificado():
    data = request.get_json()
    cert_pem = data['certificado']
    
    try:
        cert = x509.load_pem_x509_certificate(cert_pem.encode('utf-8'))
        ca_cert = x509.load_pem_x509_certificate(data['certificado_ca'].encode('utf-8'))
        
        # Verificar firma
        ca_public_key = ca_cert.public_key()
        ca_public_key.verify(
            cert.signature,
            cert.tbs_certificate_bytes,
            padding.PKCS1v15(),
            cert.signature_hash_algorithm
        )
        
        # Verificar validez temporal
        now = datetime.datetime.utcnow()
        if not (cert.not_valid_before <= now <= cert.not_valid_after):
            raise ValueError("Certificado fuera de su periodo de validez")
        
        # Función para extraer atributos del nombre
        def extract_name(name):
            return {attr.oid._name: attr.value for attr in name}
        
        return jsonify({
            'valido': True,
            'sujeto': extract_name(cert.subject),
            'emisor': extract_name(cert.issuer),
            'valido_desde': cert.not_valid_before.isoformat(),
            'valido_hasta': cert.not_valid_after.isoformat(),
            'numero_serie': str(cert.serial_number)  # Convertir a string para serialización
        })
    except Exception as e:
        return jsonify({
            'valido': False,
            'error': str(e)
        }), 400