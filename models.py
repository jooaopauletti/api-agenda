from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String,  unique = True, nullable = False)
    senha = db.Column(db.String, nullable = False)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String, nullable = False)
    telefone = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey ('usuario.id'), nullable = False)