'''9. Interface Vendavel:
Define os métodos:
calcularPrecoTotal(int quantidade) para calcular o preço total de um
produto ou serviço com base na quantidade.
aplicarDesconto(double desconto) para aplicar um desconto no preço
total.'''


from abc import ABC, abstractmethod

class Vendavel(ABC):
    @abstractmethod
    def calcularPrecoTotal(self, quantidade: int) -> float:
        pass

    @abstractmethod
    def aplicarDesconto(self, desconto: float):
        pass

class Produto(Vendavel):
    def __init__(self, nome, preco_unitario, quantidade_em_estoque):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade_em_estoque = quantidade_em_estoque

    def calcularPrecoTotal(self, quantidade: int) -> float:
        if quantidade <= self.quantidade_em_estoque:
            return quantidade * self.preco_unitario
        else:
            return -1  # Retorna -1 se a quantidade desejada não estiver disponível em estoque

    def aplicarDesconto(self, desconto: float):
        self.preco_unitario -= desconto

class Servico(Vendavel):
    def __init__(self, nome, preco_por_hora, horas_de_trabalho):
        self.nome = nome
        self.preco_por_hora = preco_por_hora
        self.horas_de_trabalho = horas_de_trabalho

    def calcularPrecoTotal(self, quantidade: int) -> float:
        return self.preco_por_hora * self.horas_de_trabalho

    def aplicarDesconto(self, desconto: float):
        self.preco_por_hora -= desconto

# Exemplo de uso das classes Produto e Servico
if __name__ == "__main__":
    # Criando um produto
    produto = Produto("Computador", 1500.0, 10)

    # Calculando o preço total de 5 unidades do produto
    quantidade_produto = 5
    preco_total_produto = produto.calcularPrecoTotal(quantidade_produto)
    print(f"Preço total de {quantidade_produto} unidades do produto: R$ {preco_total_produto:.2f}")

    # Aplicando um desconto de R$ 100 no produto
    desconto_produto = 100.0
    produto.aplicarDesconto(desconto_produto)

    # Calculando o novo preço total de 5 unidades do produto após o desconto
    novo_preco_total_produto = produto.calcularPrecoTotal(quantidade_produto)
    print(f"Novo preço total de {quantidade_produto} unidades do produto após o desconto: R$ {novo_preco_total_produto:.2f}")

    # Criando um serviço
    servico = Servico("Consultoria", 100.0, 8)

    # Calculando o preço total do serviço para 8 horas de trabalho
    preco_total_servico = servico.calcularPrecoTotal(8)
    print(f"Preço total do serviço para 8 horas de trabalho: R$ {preco_total_servico:.2f}")

    # Aplicando um desconto de R$ 20 por hora no serviço
    desconto_servico = 20.0
    servico.aplicarDesconto(desconto_servico)

    # Calculando o novo preço total do serviço para 8 horas de trabalho após o desconto
    novo_preco_total_servico = servico.calcularPrecoTotal(8)
    print(f"Novo preço total do serviço para 8 horas de trabalho após o desconto: R$ {novo_preco_total_servico:.2f}")

