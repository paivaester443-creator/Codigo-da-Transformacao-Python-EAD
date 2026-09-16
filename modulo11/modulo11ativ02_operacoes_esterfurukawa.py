import sqlite3

conn = sqlite3.connect('modulo11.db')
cursor = conn.cursor()

# 1. CREATE (Inserir)
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ('Ana Souza', 'ana@email.com'))
cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", ('Carlos Lima', 'carlos@email.com'))
conn.commit()

# 2. READ (Consultar todos)
print("--- Clientes Cadastrados ---")
cursor.execute("SELECT * FROM Clientes")
for cliente in cursor.fetchall():
    print(cliente)

# 3. UPDATE (Atualizar email do id 1)
cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", ('ana.souza@email.com', 1))
conn.commit()

# 4. DELETE (Excluir cliente do id 2)
cursor.execute("DELETE FROM Clientes WHERE id = ?", (2,))
conn.commit()

conn.close()