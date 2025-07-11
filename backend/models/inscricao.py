from utils.db_config import get_db

class Inscricao:
    def __init__(self, id, usuario_id, idade, genero, endereco, cpf, renda, dependentes, escolaridade, moradia, ocupacao, despesas):
        self.id = id
        self.usuario_id = usuario_id
        self.idade = idade
        self.genero = genero
        self.endereco = endereco
        self.cpf = cpf
        self.renda = renda
        self.dependentes = dependentes
        self.escolaridade = escolaridade
        self.moradia = moradia
        self.ocupacao = ocupacao
        self.despesas = despesas

    @staticmethod
    def create(usuario_id, idade, genero, endereco, cpf, renda, dependentes, escolaridade, moradia, ocupacao, despesas):
        db = get_db()
        cursor = db.connection.cursor()
        cursor.execute('''
            INSERT INTO inscricoes (usuario_id, idade, genero, endereco, cpf, renda, dependentes, escolaridade, moradia, ocupacao, despesas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (usuario_id, idade, genero, endereco, cpf, renda, dependentes, escolaridade, moradia, ocupacao, despesas))
        db.connection.commit()
        cursor.close()

    @staticmethod
    def find_by_usuario(usuario_id):
        db = get_db()
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM inscricoes WHERE usuario_id = %s', (usuario_id,))
        rows = cursor.fetchall()
        cursor.close()
        return [Inscricao(*row) for row in rows]
