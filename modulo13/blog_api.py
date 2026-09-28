import sqlite3
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

def init_blog_db():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY (autor_id) REFERENCES usuarios (id)
        )
    ''')
    conn.commit()
    conn.close()

# Registro de usuário
@app.route('/register', methods=['POST'])
def register():
    dados = request.get_json()
    if not dados or 'username' not in dados or 'password' not in dados:
        return jsonify({"erro": "Dados incompletos"}), 400

    hashed_pw = generate_password_hash(dados['password'])
    
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (dados['username'], hashed_pw))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({"erro": "Usuário já existe"}), 400

    conn.close()
    return jsonify({"mensagem": "Usuário registrado com sucesso!"}), 201

# Autenticação (Login)
@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, password FROM usuarios WHERE username = ?", (dados.get('username'),))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[1], dados.get('password', '')):
        return jsonify({"mensagem": "Login bem-sucedido!", "user_id": user[0]}), 200
    
    return jsonify({"erro": "Credenciais inválidas"}), 401

# Criar Post
@app.route('/posts', methods=['POST'])
def criar_post():
    dados = request.get_json()
    if not dados or 'titulo' not in dados or 'conteudo' not in dados or 'autor_id' not in dados:
        return jsonify({"erro": "Dados do post incompletos"}), 400

    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)", 
                   (dados['titulo'], dados['conteudo'], dados['autor_id']))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Post criado com sucesso!"}), 201

# Listar Posts
@app.route('/posts', methods=['GET'])
def listar_posts():
    conn = sqlite3.connect('blog.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, titulo, conteudo, autor_id FROM posts")
    posts = [{"id": row[0], "titulo": row[1], "conteudo": row[2], "autor_id": row[3]} for row in cursor.fetchall()]
    conn.close()

    return jsonify(posts), 200

if __name__ == '__main__':
    init_blog_db()
    app.run(debug=True, port=5001)