from django.test import TestCase, Client
from django.urls import reverse
from models import Produto

class ProdutoAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.produto = Produto.objects.create(
            nome="Teclado",
            descricao="Teclado Mecânico",
            preco=150.00,
            quantidade=10
        )

    def test_criar_produto(self):
        response = self.client.post(
            reverse('produtos_list_create'),
            data={"nome": "Mouse", "preco": 80.00, "quantidade": 5},
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_listar_produtos(self):
        response = self.client.get(reverse('produtos_list_create'))
        self.assertEqual(response.status_code, 200)

    def test_busca_produto(self):
        response = self.client.get(reverse('produtos_list_create') + '?nome=Teclado')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Teclado")