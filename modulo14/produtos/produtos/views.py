import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from models import Produto

# Registar e Listar Produtos
@csrf_exempt
def listar_ou_criar_produtos(request):
    if request.method == 'GET':
        busca = request.GET.get('nome', '')
        produtos_list = Produto.objects.filter(nome__icontains=busca) if busca else Produto.objects.all()

        # Paginação (Atendendo ao Desafio Extra)
        paginator = Paginator(produtos_list, 5)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        dados = [
            {
                "id": p.id,
                "nome": p.nome,
                "descricao": p.descricao,
                "preco": float(p.preco),
                "quantidade": p.quantidade
            } for p in page_obj
        ]

        return JsonResponse({
            "produtos": dados,
            "pagina_atual": page_obj.number,
            "total_paginas": paginator.num_pages,
            "total_itens": paginator.count
        }, status=200)

    elif request.method == 'POST':
        dados = json.loads(request.body)
        produto = Produto.objects.create(
            nome=dados['nome'],
            descricao=dados.get('descricao', ''),
            preco=dados['preco'],
            quantidade=dados['quantidade']
        )
        return JsonResponse({"mensagem": "Produto registado com sucesso!", "id": produto.id}, status=201)

# Detalhar, Atualizar e Eliminar Produto
@csrf_exempt
def detalhar_atualizar_deletar_produto(request, pk):
    try:
        produto = Produto.objects.get(pk=pk)
    except Produto.DoesNotExist:
        return JsonResponse({"erro": "Produto não encontrado"}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            "id": produto.id,
            "nome": produto.nome,
            "descricao": produto.descricao,
            "preco": float(produto.preco),
            "quantidade": produto.quantidade
        }, status=200)

    elif request.method == 'PUT':
        dados = json.loads(request.body)
        produto.nome = dados.get('nome', produto.nome)
        produto.descricao = dados.get('descricao', produto.descricao)
        produto.preco = dados.get('preco', produto.preco)
        produto.quantidade = dados.get('quantidade', produto.quantidade)
        produto.save()
        return JsonResponse({"mensagem": "Produto atualizado com sucesso!"}, status=200)

    elif request.method == 'DELETE':
        produto.delete()
        return JsonResponse({"mensagem": "Produto removido com sucesso!"}, status=200)