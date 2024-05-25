from abc import ABC, abstractmethod

class Pedido(ABC):
    @abstractmethod
    def obterId(self):
        pass

    @abstractmethod
    def obterCliente(self):
        pass

    @abstractmethod
    def obterDataPedido(self):
        pass

    @abstractmethod
    def obterItens(self):
        pass

    @abstractmethod
    def calcularValorTotal(self):
        pass

    @abstractmethod
    def aplicarDesconto(self, desconto):
        pass
