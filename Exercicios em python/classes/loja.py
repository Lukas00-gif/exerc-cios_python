from classes.produto import Produto
from classes.cliente import Cliente
from classes.item_pedido import ItemPedido
from classes.pedido_simples import PedidoSimples
from classes.pedido_express import PedidoExpress
from datetime import datetime

class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []
        self.pedidos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

    def criar_pedido(self, cliente, itens, tipo_pedido='simples', taxa_frete=0):
        if tipo_pedido == 'simples':
            novo_pedido = PedidoSimples(
                id=len(self.pedidos) + 1,
                cliente=cliente,
                data_pedido=datetime.now(),
                itens=itens,
                taxa_frete=taxa_frete
            )
        else:
            novo_pedido = PedidoExpress(
                id=len(self.pedidos) + 1,
                cliente=cliente,
                data_pedido=datetime.now(),
                itens=itens,
                taxa_frete_express=taxa_frete
            )
        self.pedidos.append(novo_pedido)
        return novo_pedido

    def listar_pedidos(self):
        return self.pedidos

    def obter_pedido_por_id(self, id_pedido):
        for pedido in self.pedidos:
            if pedido.obterId() == id_pedido:
                return pedido
        return None

    def calcular_faturamento_total(self):
        return sum(pedido.calcularValorTotal() for pedido in self.pedidos)
