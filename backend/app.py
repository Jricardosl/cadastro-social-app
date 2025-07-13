from flask import Flask, request, jsonify # type: ignore
from flask_mysqldb import MySQL # type: ignore
from flask_cors import CORS # type: ignore
import bcrypt # type: ignore

app = Flask(__name__)
CORS(app)

# Configuração MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Cobrakai01@'
app.config['MYSQL_DB'] = 'cadastro_social'
mysql = MySQL(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    nome = data.get('name')
    email = data.get('email')
    senha = data.get('password')

    if not nome or not email or not senha:
        return jsonify({'error': 'Campos obrigatórios faltando'}), 400

    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)",
                (nome, email, hashed_password))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Usuário cadastrado com sucesso!'})
@app.route('/form', methods=['POST'])
def salvar_formulario():
    data = request.json
    email = data.get('email')
    form = data.get('form')

    if not email or not form:
        return jsonify({'error': 'Email ou dados do formulário ausentes'}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT id FROM usuarios WHERE email = %s", (email,))
    user = cur.fetchone()
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    user_id = user[0]

    cur.execute("""
        INSERT INTO formularios (usuario_id, renda_familiar, membros_familia, despesas_mensais, escolaridade)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        user_id,
        form['renda_familiar'],
        form['membros_familia'],
        form['despesas_mensais'],
        form['escolaridade']
    ))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Formulário salvo com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)