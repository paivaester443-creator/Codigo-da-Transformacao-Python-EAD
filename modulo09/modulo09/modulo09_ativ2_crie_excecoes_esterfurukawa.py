class SaldoInsuficienteError(Exception):
    """Exceção personalizada lançada quando o saque é maior que o saldo."""

    pass


class ContaBancaria:

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero!")
        if valor > self.saldo:
            raise SaldoInsuficienteError(
                f"Saque negado! Valor solicitado: R$ {valor:.2f} | Saldo"
                f" disponível: R$ {self.saldo:.2f}"
            )

        self.saldo -= valor
        return (
            f"✅ Saque de R$ {valor:.2f} realizado com sucesso! Saldo"
            f" restante: R$ {self.saldo:.2f}"
        )


# ==========================================
# EXECUÇÃO INTERATIVA COM ENTRADA DO USUÁRIO
# ==========================================

# Definindo o saldo inicial com validação
while True:
    try:
        saldo_ini = float(input("Digite o saldo inicial da sua conta: R$ "))
        if saldo_ini < 0:
            print("❌ O saldo inicial não pode ser negativo.")
            continue
        minha_conta = ContaBancaria(saldo_inicial=saldo_ini)
        break
    except ValueError:
        print("❌ Digite um valor numérico válido!")

# Loop para realizar múltiplos saques
while True:
    print(f"\n--- SALDO ATUAL: R$ {minha_conta.saldo:.2f} ---")

    try:
        entrada = input("Digite o valor do saque (ou '0' para sair): R$ ")
        valor_saque = float(entrada.replace(",", "."))

        if valor_saque == 0:
            print("Saindo do sistema bancário... Até logo!")
            break

        # Tentativa de execução do saque
        resultado = minha_conta.sacar(valor_saque)
        print(resultado)

    except SaldoInsuficienteError as erro:
        # Captura especificamente a exceção personalizada que você criou
        print(f"❌ Erro de Saldo: {erro}")

    except ValueError as erro:
        # Captura quando o usuário digita letras ou números menores/iguais a zero
        if "maior que zero" in str(erro):
            print(f"❌ Erro de Entrada: {erro}")
        else:
            print(
                "❌ Erro de Formato: Digite apenas números válidos (ex: 50.00"
                " ou 50,00)!"
            )