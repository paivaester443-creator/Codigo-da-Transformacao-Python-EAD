from datetime import datetime

print("🏴‍☠️🏴‍☠️🏴‍☠️ DESAFIO EXTRA: SAUDAÇÃO + HORA ATUAL 🏴‍☠️🏴‍☠️🏴‍☠️")

nome = input("Digite o seu nome: ")

hora_atual = datetime.now().strftime("%H:%M")

print(f"Olá, {nome}! Agora são exatamente {hora_atual}. Seja muito bem-vindo(a)!")