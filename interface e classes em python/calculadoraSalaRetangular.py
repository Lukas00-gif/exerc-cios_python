'''
2. Classe CalculadoraSalaRetangular:
Implementa a interface CalculoGeometrico .
Contém os métodos:
calcularArea(double altura, double largura) para calcular a área de uma
sala retangular.
calcularPerimetro(double altura, double largura) para calcular o
perímetro de uma sala retangular.

'''

from abc import ABC, abstractmethod

class CalculoGeometrico(ABC):
    @abstractmethod
    def calcularArea(self, altura: float, largura: float) -> float:
        pass

    @abstractmethod
    def calcularPerimetro(self, altura: float, largura: float) -> float:
        pass

class CalculadoraSalaRetangular(CalculoGeometrico):
    def calcularArea(self, altura: float, largura: float) -> float:
        if altura < 0 or largura < 0:
            raise ValueError("A altura e a largura devem ser valores não negativos.")
        return altura * largura

    def calcularPerimetro(self, altura: float, largura: float) -> float:
        if altura < 0 or largura < 0:
            raise ValueError("A altura e a largura devem ser valores não negativos.")
        return 2 * (altura + largura)

# Exemplo de uso
if __name__ == "__main__":
    calculadora = CalculadoraSalaRetangular()
    altura = 7.59
    largura = 8.49
    area = calculadora.calcularArea(altura, largura)
    perimetro = calculadora.calcularPerimetro(altura, largura)
    print(f"A área da sala retangular é: {area} metros quadrados.")
    print(f"O perímetro da sala retangular é: {perimetro} metros.")
