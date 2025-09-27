from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome


class Marmitex(models.Model):
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.descricao


class Pedido(models.Model):
    TIPO_ENTREGA = [
        ('RETIRADA', 'Retirada imediata'),
        ('RESERVA', 'Reservado para retirada'),
        ('ENTREGA', 'Entrega'),
    ]

    TIPO_PAGAMENTO = [
        ('DINHEIRO', 'Dinheiro'),
        ('PIX', 'PIX'),
        ('CARTAO', 'Cartão'),
        ('PRAZO', 'Prazo'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marmitex = models.ForeignKey(Marmitex, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    valor_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)
    tipo_entrega = models.CharField(max_length=8, choices=TIPO_ENTREGA)
    tipo_pagamento = models.CharField(max_length=8, choices=TIPO_PAGAMENTO)
    reservado = models.BooleanField(default=False)
    retirado = models.BooleanField(default=False)
    data_pedido = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField(blank=True, null=True)


def save(self, *args, **kwargs):
    # Calcula valor_total automaticamente
    self.valor_total = self.valor_unitario * self.quantidade
    super().save(*args, **kwargs)


def __str__(self):
    return f"Pedido #{self.id} - {self.cliente.nome} ({self.get_tipo_entrega_display()})"
