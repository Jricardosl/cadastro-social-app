from flask_mysqldb import MySQL # type: ignore
from flask import current_app, g # type: ignore

def init_db(app):
    mysql = MySQL(app)
    return mysql

def get_db():
    if 'db' not in g:
        g.db = current_app.extensions['mysql']
    return g.db
