from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # Valor total será 'readonly'
    self.fields['valor_total'].widget.attrs['readonly'] = True
    # Opcional: valor unitário inicial conforme marmitex
    if 'marmitex' in self.initial:
        marmitex_obj = self.initial['marmitex']
        self.fields['valor_unitario'].initial = marmitex_obj.preco
