import random

# 1. Definindo naipes e valores
naipes = ["Copas", "Espadas", "Ouros", "Paus"]
valores = ["Ás", "10", "Valete", "Dama", "Rei", "9"]

# 2. Criando o baralho com as 24 combinações
baralho = []
for valor in valores:
    for naipe in naipes:
        baralho.append(f"{valor} de {naipe}")

# 3. Sorteando a carta secreta inicial
carta_secreta = random.choice(baralho)

print("🃏 Bem-vindo ao Jogo de Adivinhação de Cartas!")
print("Tente adivinhar a carta secreta (exemplo: 'Ás de Copas').\n")

# 4. Loop de 6 tentativas
for tentativa in range(1, 7):
    print(f"--- Tentativa {tentativa} de 6 ---")
    chute = input("Qual é o seu palpite? ").strip()

    # 5. Regra especial: na 6ª tentativa, a carta secreta vira o chute!
    if tentativa == 6:
        carta_secreta = chute

    # 6. Verificação do palpite
    if chute.lower() == carta_secreta.lower():
        print(f"🎉 Parabéns! Você acertou! A carta secreta era '{carta_secreta}'.")
        break
    else:
        print("❌ Errou!")