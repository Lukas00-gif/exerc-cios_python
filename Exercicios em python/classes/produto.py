class Produto:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def obter_nome(self):
        return self.nome

    def obter_descricao(self):
        return self.descricao

    def obter_preco(self):
        return self.preco
