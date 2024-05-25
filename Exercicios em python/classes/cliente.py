class Cliente:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def obter_nome(self):
        return self.nome

    def obter_endereco(self):
        return self.endereco
