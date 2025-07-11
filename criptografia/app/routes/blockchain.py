from flask import Blueprint, render_template, request
import hashlib
import time
from flask import jsonify


bp = Blueprint('blockchain', __name__, url_prefix='/blockchain')

# Clase básica para el bloque
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

# Crear un bloque
def create_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = str(int(time.time()))  # Time as string
    hash_value = hashlib.sha256(f"{index}{previous_block.hash}{timestamp}{data}".encode()).hexdigest()
    block = Block(index, previous_block.hash, timestamp, data, hash_value)
    return block

# Crear la cadena de bloques inicial
def create_genesis_block():
    return Block(0, "0", "2025-01-01", "Genesis Block", hashlib.sha256("Genesis Block".encode()).hexdigest())

# Blockchain básico
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Ruta principal para Blockchain
@bp.route('/')
def index():
    return render_template('blockchain/index.html', blockchain=blockchain)

# Ruta para la demostración de Blockchain
@bp.route('/demostracion')
def demostracion():
    return render_template('blockchain/demostracion.html', blockchain=blockchain)

# Ruta para añadir un bloque a la cadena
@bp.route('/add_block', methods=['POST'])
def add_block():
    data = request.form['data']
    new_block = create_block(previous_block, data)
    blockchain.append(new_block)
    return render_template('blockchain/index.html', blockchain=blockchain)

# Ruta para obtener la cadena de bloques en formato JSON
@bp.route('/blockchain_data')
def blockchain_data():
    chain_data = [{"index": block.index, "data": block.data} for block in blockchain]
    return jsonify(chain_data)
