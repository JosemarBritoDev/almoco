from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Pedido
from .forms import PedidoForm
from django.http import JsonResponse
from .models import Marmitex


class PedidoListView(ListView):
    model = Pedido
    template_name = 'core/pedido_list.html'
    context_object_name = 'pedidos'


class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'core/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'core/pedido_form.html'
    success_url = reverse_lazy('pedido_list')


def get_marmitex_preco(request, marmitex_id):
    marmitex = Marmitex.objects.get(id=marmitex_id)
    return JsonResponse({'preco': float(marmitex.preco)})
