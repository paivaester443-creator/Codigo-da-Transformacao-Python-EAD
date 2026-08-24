agenda = {}

while True:
    print("\n---🏴‍☠️ AGENDA DE CONTATOS 🏴‍☠️---")
    print("1. Adicionar contato")
    print("2. Remover contato")
    print("3. Buscar contato")
    print("4. Visualizar todos os contatos")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do contato: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        agenda[nome] = {"telefone": telefone, "email": email}
        print(f"Contato '{nome}' adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do contato a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"Contato '{nome}' removido.")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Nome do contato a buscar: ").strip()
        if nome in agenda:
            print(f"\nNome: {nome}")
            print(f"Telefone: {agenda[nome]['telefone']}")
            print(f"E-mail: {agenda[nome]['email']}")
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        if not agenda:
            print("A agenda está vazia.")
        else:
            print("\nLista de Contatos:")
            for nome, info in agenda.items():
                print(f"- {nome}: Tel: {info['telefone']} | Email: {info['email']}")

    elif opcao == "5":
        print("Saindo da agenda...")
        break
    else:
        print("Opção inválida! Tente novamente.")