import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# Configuração e inicialização do banco SQLite
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 1. Rota GET /saudacao
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá! Seja bem-vindo à API."}), 200

# 2 e 3. Rota POST /cadastrar com persistência no SQLite
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()

    if not dados or 'nome' not in dados or 'email' not in dados:
        return jsonify({"erro": "Envie 'nome' e 'email' no formato JSON."}), 400

    nome = dados['nome']
    email = dados['email']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

if __name__ == '__main__':
    init_db()
    app.run(debug=True)