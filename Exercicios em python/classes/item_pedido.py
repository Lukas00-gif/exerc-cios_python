from classes.produto import Produto

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def obter_produto(self):
        return self.produto

    def obter_quantidade(self):
        return self.quantidade

    def obter_preco_unitario(self):
        return self.produto.obter_preco()

    def calcular_valor_total(self):
        return self.quantidade * self.produto.obter_preco()
