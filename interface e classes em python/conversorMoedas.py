'''

1. Classe ConversorMoeda:
Implementa a interface ConversaoFinanceira .
Contém o método converterDolarParaReal(double valorDolar) para converter um
valor em dólar para real.
O método deve receber o valor em dólar como parâmetro e utilizar a taxa de
câmbio atual para realizar a conversão.

'''

from abc import ABC, abstractmethod

class ConversaoFinanceira(ABC):
    @abstractmethod
    def converterDolarParaReal(self, valorDolar: float) -> float:
        pass

class ConversorMoeda(ConversaoFinanceira):
    TAXA_CAMBIO = 5.20  # 1 USD = 5.20 BRL

    def converterDolarParaReal(self, valorDolar: float) -> float:
        if valorDolar < 0:
            raise ValueError("O valor em dólar não pode ser negativo.")
        valorReal = valorDolar * self.TAXA_CAMBIO
        return valorReal

if __name__ == "__main__":
    conversor = ConversorMoeda()
    valorDolar = 6000
    valorReal = conversor.converterDolarParaReal(valorDolar)
    print(f"{valorDolar} dólares equivalem a {valorReal} reais.")
