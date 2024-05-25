'''Classe TabuadaMultiplicacao:
Implementa a interface Tabuada .
Contém o método mostrarTabuada(int numero) para exibir a tabuada de um número.
O método deve mostrar a tabuada do número de 1 a 10.
'''

from abc import ABC, abstractmethod

class Tabuada(ABC):
    @abstractmethod
    def mostrarTabuada(self, numero: int):
        pass

class TabuadaMultiplicacao(Tabuada):
    def mostrarTabuada(self, numero: int):
        if numero < 0:
            raise ValueError("O número deve ser não negativo.")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")

# Exemplo de uso
if __name__ == "__main__":
    tabuada = TabuadaMultiplicacao()
    numero = 4
    tabuada.mostrarTabuada(numero)
