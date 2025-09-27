from django.urls import path
from .views import PedidoListView, PedidoCreateView, PedidoUpdateView
from .views import get_marmitex_preco

urlpatterns = [
    path('pedidos/', PedidoListView.as_view(), name='pedido_list'),
    path('pedidos/cadastrar/', PedidoCreateView.as_view(), name='pedido_cadastrar'),
    path('pedidos/<int:pk>/editar/', PedidoUpdateView.as_view(), name='pedido_editar'),
    path('get_marmitex_preco/<int:marmitex_id>/', get_marmitex_preco, name='get_marmitex_preco')
]
