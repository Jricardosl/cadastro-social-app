from utils.db_config import init_db

app = Flask(__name__)
# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''  # sua senha do MySQL
app.config['MYSQL_DB'] = 'cadastro_social'

mysql = init_db(app)


from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return 'API do Cadastro Social funcionando!'

if __name__ == '__main__':
    app.run(debug=True)

from routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)

from routes.inscricao_routes import inscricao_bp # type: ignore

app.register_blueprint(inscricao_bp)
