'''6. Interface Calculavel:
Define o método calcularPrecoFinal() para calcular o preço final de um produto
ou serviço. 

um serviço qualquer com desconto + 
o produto fisico +
preço final de um livro com desconto 
'''

from abc import ABC, abstractmethod

class Calculavel(ABC):
    @abstractmethod
    def calcularPrecoFinal(self) -> float:
        pass


class Servico(Calculavel):
    def __init__(self, titulo, horas_trabalhadas, preco_por_hora):
        self.tiulo = titulo
        self.horas_trabalhadas = horas_trabalhadas
        self.preco_por_hora = preco_por_hora
    
    def calcularPrecoFinal(self):
        return self.horas_trabalhadas * self.preco_por_hora


class ProdutoFisico(Calculavel):
    def __init__(self, nome, preco_base, custo_envio, taxa_imposto):
        self.nome = nome
        self.preco_base = preco_base
        self.custo_envio = custo_envio
        self.taxa_imposto = taxa_imposto

    def calcularPrecoFinal(self) -> float:
        preco_sem_imposto = self.preco_base + self.custo_envio
        imposto = preco_sem_imposto * self.taxa_imposto
        return preco_sem_imposto + imposto


class Livro(Calculavel):
    def __init__(self, titulo, preco_base, desconto):
        self.titulo = titulo
        self.preco_base = preco_base
        self.desconto = desconto

    def calcularPrecoFinal(self) -> float:
        return self.preco_base * (1 - self.desconto)


#Servico | servico de consultoria de 8horas por 100 reais
servico = Servico("consultoria", 20, 345.0)
preco_servico = servico.calcularPrecoFinal()
print(f"Preço final do servico e: R$ {preco_servico:.2f}")

# Smartphone de R$ 2330, com R$ 40 de custo de envio e 25% de imposto
produto_fisico = ProdutoFisico("Smartphone", 2330.0, 40.0, 0.25)
preco_produto_fisico = produto_fisico.calcularPrecoFinal()
print(f"Preço final do produto físico: R$ {preco_produto_fisico:.2f}")

#livro
livro = Livro("Python Programming & Data Science", 167.0, 0.15) 
preco_final = livro.calcularPrecoFinal()
print(f"Preço final do livro: R$ {preco_final:.2f} com {livro.desconto} de desconto")

