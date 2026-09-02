def calculadora_divisao(numerador, denominador):
    """
    Função para realizar a divisão de dois números com tratamento de erros.
    """
    try:
        resultado = numerador / denominador
        return f"✅ Resultado da divisão: {resultado}"
    except ZeroDivisionError:
        return "❌ Erro: Não é possível realizar divisão por zero!"


# Loop principal para permitir entradas dinâmicas do usuário
while True:
    print("\n=== CALCULADORA DE DIVISÃO ===")
    
    try:
        num = float(input("Digite o numerador: "))
        den = float(input("Digite o denominador: "))

        # Chama a função com os valores inseridos
        mensagem = calculadora_divisao(num, den)
        print(mensagem)

    except ValueError:
        print("❌ Erro: Por favor, digite apenas números válidos!")

    # Pergunta se o usuário quer realizar outra operação
    opcao = input("\nDeseja fazer outra divisão? (S/N): ").strip().upper()
    if opcao != 'S':
        print("Encerrando a calculadora... Até mais!")
        break