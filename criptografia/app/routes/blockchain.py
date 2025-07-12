from flask import Blueprint, render_template, request, redirect, url_for
import hashlib
import json

bp = Blueprint('blockchain', __name__, url_prefix='/blockchain')

# Simulamos una blockchain simple
blockchain = [
    {
        'index': 0,
        'transactions': [],
        'proof': 100,
        'previous_hash': '0',
        'hash': 'genesis_hash'
    }
]
current_transactions = []

def hash_block(block):
    block_string = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(block_string).hexdigest()

@bp.route('/')
def index():
    return render_template('blockchain/index.html')

@bp.route('/demostracion')
def demostracion():
    return render_template('blockchain/demostracion.html', 
                         blockchain=blockchain,
                         current_transactions=current_transactions)

@bp.route('/add_transaction', methods=['POST'])
def add_transaction():
    sender = request.form.get('sender')
    recipient = request.form.get('recipient')
    amount = request.form.get('amount')
    
    if sender and recipient and amount:
        current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
    
    return redirect(url_for('blockchain.demostracion'))

@bp.route('/mine')
def mine():
    global blockchain, current_transactions
    
    last_block = blockchain[-1]
    
    # Simulamos un proof of work muy simple
    proof = 12345
    
    # Creamos el nuevo bloque
    new_block = {
        'index': len(blockchain),
        'transactions': current_transactions,
        'proof': proof,
        'previous_hash': last_block['hash'],
        'hash': 'simulated_hash_' + str(len(blockchain))
    }
    
    blockchain.append(new_block)
    current_transactions = []
    
    return redirect(url_for('blockchain.demostracion'))