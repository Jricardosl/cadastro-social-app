from utils.db_config import get_db

class User:
    def __init__(self, id, nome, email, senha):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha

    @staticmethod
    def find_by_email(email):
        db = get_db()
        cursor = db.connection.cursor()
        cursor.execute('SELECT id, nome, email, senha FROM usuarios WHERE email = %s', (email,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row)
        return None

    @staticmethod
    def create(nome, email, senha):
        db = get_db()
        cursor = db.connection.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, senha))
        db.connection.commit()
        cursor.close()
