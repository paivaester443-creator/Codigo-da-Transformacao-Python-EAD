from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.listar_ou_criar_produtos, name='produtos_list_create'),
    path('produtos/<int:pk>/', views.detalhar_atualizar_deletar_produto, name='produto_detail_update_delete'),
]