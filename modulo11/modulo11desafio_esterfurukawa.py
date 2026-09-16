import sqlite3

conn = sqlite3.connect('gerenciador_tarefas.db')
cursor = conn.cursor()

# 1. Criar Tabela de Tarefas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')
conn.commit()

# 2. Adicionar Tarefas
cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", ("Finalizar módulo 11",))
cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", ("Subir código para o GitHub",))
conn.commit()

# 3. Visualizar Tarefas
print("--- LISTA DE TAREFAS ---")
cursor.execute("SELECT * FROM tarefas")
for id_tarefa, desc in cursor.fetchall():
    print(f"[{id_tarefa}] {desc}")

# 4. Excluir Tarefa
cursor.execute("DELETE FROM tarefas WHERE id = ?", (1,))
conn.commit()

print("\n--- TAREFAS APÓS EXCLUSÃO ---")
cursor.execute("SELECT * FROM tarefas")
for id_tarefa, desc in cursor.fetchall():
    print(f"[{id_tarefa}] {desc}")

conn.close()