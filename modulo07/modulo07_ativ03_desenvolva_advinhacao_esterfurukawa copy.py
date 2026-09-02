import math
import random


def jogo_adivinhacao():
    while True:
        limite_inferior = 1
        limite_superior = 24

        tentativas_max = math.ceil(math.log2(limite_superior)) + 1
        numero_secreto = random.randint(limite_inferior, limite_superior)

        print("\n" + "=" * 45)
        print("=== 🏴‍☠️  Jogo de Adivinhação das Cartas (1 a 24) 🏴‍☠️  ===")
        print("=" * 45)
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

        # Pergunta ao jogador se deseja continuar
        jogar_denovo = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if jogar_denovo != 'S':
            print("\nObrigado por jogar! Até a próxima! 👋")
            break


jogo_adivinhacao()