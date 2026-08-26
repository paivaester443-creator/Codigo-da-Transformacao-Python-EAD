'''
Isso é um Bloco de Comentário.
>>projeto açaiteria:

>PO (Como dono do negocio: Quero um sistema de vendas para minha açaiteria,
para que eu possa disponibilizar meus produtos virtualmente.)

>QA (Como cliente: Quero um sistema de vendas para minha açaiteria,
para que eu possa comparar meus produtos com qualidade e praticidade.)

>Tech (Como programador: Quero um sistema de vendas para minha açateria,
para que eu possa desenvolver um software eficiente e funcional para o négocio.)

>Dev (Como programador: Quero um sistema de vendas para minha açaiteria,
para que eu possa implementar as funcionalidades necessárias para
atender as necessidades do negócio e dos clientes.)

>UX (Como designer de experiência do usuária: Quero um sistema de vendas
para minha açaiteria, para que eu possa criar uma interface intuitiva
e agradável para os usuários, garantindo uma experiência de compra
satisfatória.)

>IA (Como analista de dados: Quero um sistema de vendas para minha
açaiteria, para que eu possa coletar e analisar os dados de acesso
do usuário, identificando os erros e aprimorando o sistema.)
'''

# Isso é um Comentário em Linha, Finalmente quebramos a maldição.
# print('Olá, Mundo!')

p1_nome = "Açaí comum"
p1_estoque = 120
p1_preco = 14.99
p1_validade = "02/07/2027"
p1_descricao = "Açaí comum, ideal para quem não precisa de mais que o necessário."

p2_nome = "Açaí premium"
p2_estoque = 90
p2_preco = 19.99
p2_validade = "02/11/2027"
p2_descricao = "Açaí premium, uma experiência marcante e única com a melhor qualidade."

p3_nome = "Açaí personalizável"
p3_estoque = 150
p3_preco = 18.99
p3_validade = "08/06/2027"
p3_descricao = "Açaí personalizável, monte e escolha seus acompanhamentos de acordo com as suas preferências."

p4_nome = "Açaí puro"
p4_estoque = 80
p4_preco = 10.99
p4_validade = "05/10/2027"
p4_descricao = "Açaí puro, o verdadeiro sabor da Amazônia: polpa super densa, cremosa e pura."

p5_nome = "Açaí com Morango"
p5_estoque = 60
p5_preco = 15.99
p5_validade = "20/08/2027"
p5_descricao = "Açaí com morango, massa batida na fórmula com o toque fresco e leve da fruta."

while True:
    print('\n================================================================================\n')
    print('Bem-vindo ao projeto de desenvolvimento de um sistema de vendas para a açaiteria!')
    print('1- Cadastrar produto')
    print('2- Listar produtos')
    print('3- Selecionar produto')
    print('4- Cadastrar pagamento')
    print('5- Confirmar compra')
    print('6- Realizar venda')
    print('0- Sair')
    print('\n================================================================================\n')

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Cadastrando produtos...\n')
        vaga = input('Em qual vaga deseja cadastrar o produto? (1, 2, 3, 4 ou 5): ')
        
        if vaga == '1':
            p1_nome = input('Digite o nome do produto: ')
            p1_estoque = int(input('Digite a quantidade em estoque: '))
            p1_preco = float(input('Digite o preço do produto: '))
            p1_validade = input('Digite a validade do produto: ')
            p1_descricao = input('Digite a descrição do produto: ')
            print(f'\nProduto "{p1_nome}" cadastrado na vaga 1!')
            
        elif vaga == '2':
            p2_nome = input('Digite o nome do produto: ')
            p2_estoque = int(input('Digite a quantidade em estoque: '))
            p2_preco = float(input('Digite o preço do produto: '))
            p2_validade = input('Digite a validade do produto: ')
            p2_descricao = input('Digite a descrição do produto: ')
            print(f'\nProduto "{p2_nome}" cadastrado na vaga 2!')
            
        elif vaga == '3':
            p3_nome = input('Digite o nome do produto: ')
            p3_estoque = int(input('Digite a quantidade em estoque: '))
            p3_preco = float(input('Digite o preço do produto: '))
            p3_validade = input('Digite a validade do produto: ')
            p3_descricao = input('Digite a descrição do produto: ')
            print(f'\nProduto "{p3_nome}" cadastrado na vaga 3!')

        elif vaga == '4':
            p4_nome = input('Digite o nome do produto: ')
            p4_estoque = int(input('Digite a quantidade em estoque: '))
            p4_preco = float(input('Digite o preço do produto: '))
            p4_validade = input('Digite a validade do produto: ')
            p4_descricao = input('Digite a descrição do produto: ')
            print(f'\nProduto "{p4_nome}" cadastrado na vaga 4!')

        elif vaga == '5':
            p5_nome = input('Digite o nome do produto: ')
            p5_estoque = int(input('Digite a quantidade em estoque: '))
            p5_preco = float(input('Digite o preço do produto: '))
            p5_validade = input('Digite a validade do produto: ')
            p5_descricao = input('Digite a descrição do produto: ')
            print(f'\nProduto "{p5_nome}" cadastrado na vaga 5!')
            
        else:
            print('vaga inválida ou sistema cheio!')

    elif opcao == '2':
        print('Listando produtos....')
        
        if 'p1_nome' not in locals() and 'p2_nome' not in locals() and 'p3_nome' not in locals() and 'p4_nome' not in locals() and 'p5_nome' not in locals():
            print('nenhum produto cadastrado no sistema ainda.')
            
        else:
            if 'p1_nome' in locals():
                print(f"nome: {p1_nome} | preço: R$ {p1_preco:.2f} | estoque: {p1_estoque} unid.")
                print(f"validade: {p1_validade} | descrição: {p1_descricao}")
                print('-' * 30)
                
            if 'p2_nome' in locals():
                print(f"nome: {p2_nome} | preço: R$ {p2_preco:.2f} | estoque: {p2_estoque} unid.")
                print(f"validade: {p2_validade} | descrição: {p2_descricao}")
                print('-' * 30)
                
            if 'p3_nome' in locals():
                print(f"nome: {p3_nome} | preço: R$ {p3_preco:.2f} | estoque: {p3_estoque} unid.")
                print(f"validade: {p3_validade} | descrição: {p3_descricao}")
                print('-' * 30)

            if 'p4_nome' in locals():
                print(f"nome: {p4_nome} | preço: R$ {p4_preco:.2f} | estoque: {p4_estoque} unid.")
                print(f"validade: {p4_validade} | descrição: {p4_descricao}")
                print('-' * 30)

            if 'p5_nome' in locals():
                print(f"nome: {p5_nome} | preço: R$ {p5_preco:.2f} | estoque: {p5_estoque} unid.")
                print(f"validade: {p5_validade} | descrição: {p5_descricao}")
                print('-' * 30)

    elif opcao == '3':
        print('Selecionar produto.')
        selecione_produto = input('Digite o produto selecionado: ')

    elif opcao == '4':
        print('Opção 4- Cadastrar pagamento.')
        forma_pagamento = input('Digite a forma de pagamento: ')

    elif opcao == '5':
        print('Opção 5- Confirmar compra.')
        confirme_produto = input('Digite a confirmação: ')
        if confirme_produto.upper() == "SIM":
            print("Compra confirmada!")
        else:
            print("Compra cancelada!")

    elif opcao == '6':
        print('Opção 6- Realizar venda.')
        realize_venda = input('Digite "OK" para confirmar a venda: ')
        if realize_venda == 'OK':
            print('Venda realizada!🌟')
        else:
            print('Tente novamente...')

    elif opcao == '0':
        print('Opção 0- Sair.')
        break
        
    else:
        print('Opção inválida.')