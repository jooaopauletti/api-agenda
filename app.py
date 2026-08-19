from flask import Flask, jsonify, request, session
from models import db, Contato, Usuario
from dotenv import load_dotenv
import os
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
DB_NAME = 'apiagenda.db'

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/contatos', methods=['GET'])
def listar_contatos():
    if 'usuario_id' not in session:
        return jsonify({'erro': 'não autenticado'}), 401
    
    contatos = Contato.query.filter_by(usuario_id=session['usuario_id']).all()
    
    lista = []
    for contato in contatos:
        lista.append({
            'id': contato.id,
            'nome': contato.nome,
            'telefone': contato.telefone,
            'email': contato.email
        })
    
    return jsonify(lista)

@app.route('/login', methods =['POST'])
def login():
    dados = request.get_json()
    login = dados['login'].strip()
    senha = dados['senha'].strip()

    usuario = Usuario.query.filter_by(login=login).first()

    if usuario and check_password_hash(usuario.senha, senha):
        session['usuario_id'] = usuario.id
        return jsonify({'mensagem': 'Login realizado com sucesso!'}), 200
    
    return jsonify({'erro': 'Login ou senha inválidos'}), 401

@app.route('/cadastro', methods=['POST'])
def cadastro():
    dados = request.get_json()
    login = dados['login'].strip()
    senha = dados['senha'].strip()
    senha_hash = generate_password_hash(senha)
    novo_usuario = Usuario(login=login, senha=senha_hash)
    db.session.add(novo_usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Cadastro realizado com sucesso!'}), 201

@app.route('/contatos', methods=['POST'])
def adicionar():
    if 'usuario_id' not in session:
        return jsonify({'erro': 'Faça o login!'}), 401
    dados = request.get_json()
    nome = dados['nome'].strip()
    telefone = dados['telefone'].strip()
    email = dados['email'].strip()    
    novo_contato = Contato(nome=nome, email=email, telefone=telefone, usuario_id=session['usuario_id'])
    db.session.add(novo_contato)
    db.session.commit()
    return jsonify({'mensagem': 'Contato adicionado com sucesso!'}), 201

@app.route('/contatos/<int:id>', methods=['GET'])
def buscar_contato(id):
    if 'usuario_id' not in session:
        return jsonify({'erro': 'não autenticado'}), 401
    
    contato = Contato.query.filter_by(id=id, usuario_id=session['usuario_id']).first()

    if contato is None:
        return jsonify({'Erro!': 'Contato não localizado!'}), 404

    return jsonify({'id': contato.id, 'nome': contato.nome, 'telefone': contato.telefone, 'email': contato.email}), 200




if __name__ == '__main__':
    app.run(debug=True)