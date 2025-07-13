from flask import Blueprint, request, jsonify # type: ignore
from utils.db_config import get_db
from models.inscricao import Inscricao

inscricao_bp = Blueprint('inscricao', __name__, url_prefix='/inscricao')

@inscricao_bp.route('/create', methods=['POST'])
def create_inscricao():
    data = request.json
    required_fields = ['usuario_id', 'idade', 'genero', 'endereco', 'cpf', 'renda', 'dependentes', 'escolaridade', 'moradia', 'ocupacao', 'despesas']

    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400

    Inscricao.create(
        usuario_id=data['usuario_id'],
        idade=data['idade'],
        genero=data['genero'],
        endereco=data['endereco'],
        cpf=data['cpf'],
        renda=data['renda'],
        dependentes=data['dependentes'],
        escolaridade=data['escolaridade'],
        moradia=data['moradia'],
        ocupacao=data['ocupacao'],
        despesas=data['despesas']
    )

    return jsonify({'message': 'Inscrição criada com sucesso'}), 201

@inscricao_bp.route('/usuario/<int:usuario_id>', methods=['GET'])
def get_inscricoes_usuario(usuario_id):
    inscricoes = Inscricao.find_by_usuario(usuario_id)
    result = []
    for i in inscricoes:
        result.append({
            'id': i.id,
            'usuario_id': i.usuario_id,
            'idade': i.idade,
            'genero': i.genero,
            'endereco': i.endereco,
            'cpf': i.cpf,
            'renda': float(i.renda),
            'dependentes': i.dependentes,
            'escolaridade': i.escolaridade,
            'moradia': i.moradia,
            'ocupacao': i.ocupacao,
            'despesas': float(i.despesas)
        })
    return jsonify(result), 200

from flask import send_file # type: ignore
from utils.pdf_generator import generate_pdf

@inscricao_bp.route('/pdf/<int:inscricao_id>', methods=['GET'])
def get_pdf(inscricao_id):
    db = get_db()
    cursor = db.connection.cursor()
    cursor.execute('SELECT * FROM inscricoes WHERE id = %s', (inscricao_id,))
    row = cursor.fetchone()
    cursor.close()

    if not row:
        return jsonify({'error': 'Inscrição não encontrada'}), 404

    # Monta dict com os dados da inscrição
    columns = ['id', 'usuario_id', 'idade', 'genero', 'endereco', 'cpf', 'renda', 'dependentes', 'escolaridade', 'moradia', 'ocupacao', 'despesas']
    inscricao = dict(zip(columns, row))

    pdf_buffer = generate_pdf(inscricao)

    return send_file(pdf_buffer, as_attachment=True, download_name=f"inscricao_{inscricao_id}.pdf", mimetype='application/pdf')
