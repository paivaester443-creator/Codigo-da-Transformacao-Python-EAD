import math
import random


def jogo_adivinhacao():
    limite_inferior = 1
    limite_superior = 24

    # Utiliza math.ceil e math.log2 para calcular a base de tentativas + margem (resulta em 6)
    tentativas_max = math.ceil(math.log2(limite_superior)) + 1
    numero_secreto = random.randint(limite_inferior, limite_superior)

    print("=== Jogo de Adivinhação das Cartas (1 a 24) ===")
    print(f"Você tem até {tentativas_max} tentativas para adivinhar a carta secreta!\n")

    tentativas = 0
    while tentativas < tentativas_max:
        tentativas += 1
        chute = int(input(f"Tentativa {tentativas}/{tentativas_max} - Digite seu palpite (1 a 24): "))

        if chute == numero_secreto:
            print(f"🎉 Parabéns! Você acertou a carta {numero_secreto} em {tentativas} tentativa(s)!")
            break
        elif chute < numero_secreto:
            print("💡 Dica: A carta secreta é MAIOR.\n")
        else:
            print("💡 Dica: A carta secreta é MENOR.\n")
    else:
        print(f"❌ Fim de jogo! A carta secreta era {numero_secreto}.")


jogo_adivinhacao()