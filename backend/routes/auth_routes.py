from flask import Blueprint, request, jsonify, current_app # type: ignore
from werkzeug.security import generate_password_hash, check_password_hash # type: ignore
import jwt # type: ignore
import datetime

from utils.db_config import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')

    if not nome or not email or not senha:
        return jsonify({'error': 'Nome, email e senha são obrigatórios'}), 400

    db = get_db()
    cursor = db.connection.cursor()

    # Verificar se o email já existe
    cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
    user = cursor.fetchone()
    if user:
        return jsonify({'error': 'Email já cadastrado'}), 400

    # Criptografar senha
    hashed_password = generate_password_hash(senha)
