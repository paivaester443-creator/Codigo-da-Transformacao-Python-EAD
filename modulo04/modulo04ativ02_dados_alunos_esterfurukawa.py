aluno = {
    "nome": "Ana Silva",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print("=== DADOS DO ALUNO ===")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")

media = sum(aluno['notas']) / len(aluno['notas'])
print(f"Média do aluno: {media:.2f}")