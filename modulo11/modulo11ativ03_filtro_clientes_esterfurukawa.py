import sqlite3

conn = sqlite3.connect('modulo11.db')
cursor = conn.cursor()

# Inserindo dados de teste
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ('Arthur Pendelton', 'arthur@email.com'))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ('Beatriz Silva', 'beatriz@email.com'))
conn.commit()

# Consulta filtrada (Nomes iniciados com 'A')
print("--- Clientes com nome começando em 'A' ---")
cursor.execute("SELECT * FROM Clientes WHERE nome LIKE 'A%'")

for cliente in cursor.fetchall():
    print(cliente)

conn.close()