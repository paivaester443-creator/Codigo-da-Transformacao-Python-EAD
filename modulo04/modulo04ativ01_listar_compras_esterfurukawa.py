lista_compras = []

while True:
    print("\n--- LISTA DE COMPRAS ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Visualizar lista")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a ser adicionado: ").strip()
        if item:
            lista_compras.append(item)
            print(f"'{item}' foi adicionado à lista.")
    elif opcao == "2":
        item = input("Digite o item a ser removido: ").strip()
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' foi removido da lista.")
        else:
            print("Item não encontrado na lista.")
    elif opcao == "3":
        print("\nItens na lista:")
        if not lista_compras:
            print("A lista está vazia.")
        else:
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}. {item}")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida! Tente novamente.")