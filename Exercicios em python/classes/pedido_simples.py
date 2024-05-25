# classes/pedido_simples.py

from interfaces.pedido import Pedido
from datetime import datetime
from classes.item_pedido import ItemPedido
from classes.cliente import Cliente

class PedidoSimples(Pedido):
    def __init__(self, id, cliente, data_pedido, itens, taxa_frete):
        self.id = id
        self.cliente = cliente
        self.data_pedido = data_pedido
        self.itens = itens
        self.taxa_frete = taxa_frete
        self.desconto = 0

    def obterId(self):
        return self.id

    def obterCliente(self):
        return self.cliente

    def obterDataPedido(self):
        return self.data_pedido

    def obterItens(self):
        return self.itens

    def calcularValorTotal(self):
        total = sum(item.calcular_valor_total() for item in self.itens)
        total_com_frete = total + self.taxa_frete
        total_com_desconto = total_com_frete * (1 - self.desconto / 100)
        return total_com_desconto

    def aplicarDesconto(self, desconto):
        self.desconto = desconto
