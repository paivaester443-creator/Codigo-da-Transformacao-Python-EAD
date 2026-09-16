import sqlite3

# Conexão com o banco de dados SQLite
conn = sqlite3.connect('modulo11.db')
cursor = conn.cursor()

# Criação da tabela Clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Tabela 'Clientes' criada com sucesso!")