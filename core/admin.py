from django.contrib import admin
from .models import Cliente, Marmitex, Pedido
from .forms import PedidoForm


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'endereco')
    search_fields = ('nome', 'telefone')


@admin.register(Marmitex)
class MarmitexAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco')
    search_fields = ('descricao',)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    form = PedidoForm
    list_display = (
        'id', 'cliente', 'marmitex', 'quantidade', 'tipo_entrega',
        'tipo_pagamento', 'valor_total', 'reservado', 'retirado', 'data_pedido'
    )
    list_filter = ('tipo_entrega', 'tipo_pagamento', 'reservado', 'retirado')
    search_fields = ('cliente__nome', 'marmitex__descricao', 'id')
    actions = ['marcar_como_retirado']

    # Adiciona JS para cálculo dinâmico
    class Media:
        js = ('core/pedido.js',)  # Crie este JS em core/static/core/pedido.js


def marcar_como_retirado(self, request, queryset):
    queryset.update(retirado=True, reservado=False)
    self.message_user(request, "Pedidos marcados como retirados!")
    marcar_como_retirado.short_description = "Marcar pedidos selecionados como retirados"
