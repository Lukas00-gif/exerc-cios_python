'''
5. Classe ConversorTemperaturaPadrao:
Implementa a interface ConversorTemperatura .
Fornece as implementações para os métodos de conversão de temperatura
utilizando as fórmulas padrão.

usando a biblioteca pint do python
'''
from abc import ABC, abstractmethod
import pint

class ConversorTemperatura(ABC):
    @abstractmethod
    def celsiusParaFahrenheit(self, celsius: float) -> float:
        pass

    @abstractmethod
    def fahrenheitParaCelsius(self, fahrenheit: float) -> float:
        pass

    @abstractmethod
    def celsiusParaKelvin(self, celsius: float) -> float:
        pass

    @abstractmethod
    def kelvinParaCelsius(self, kelvin: float) -> float:
        pass

    @abstractmethod
    def fahrenheitParaKelvin(self, fahrenheit: float) -> float:
        pass

    @abstractmethod
    def kelvinParaFahrenheit(self, kelvin: float) -> float:
        pass

class ConversorTemperaturaPadrao(ConversorTemperatura):
    def __init__(self):
        self.ureg = pint.UnitRegistry()
        self.Q_ = self.ureg.Quantity

    def celsiusParaFahrenheit(self, celsius: float) -> float:
        return self.Q_(celsius, 'degC').to('degF').magnitude

    def fahrenheitParaCelsius(self, fahrenheit: float) -> float:
        return self.Q_(fahrenheit, 'degF').to('degC').magnitude

    def celsiusParaKelvin(self, celsius: float) -> float:
        return self.Q_(celsius, 'degC').to('kelvin').magnitude

    def kelvinParaCelsius(self, kelvin: float) -> float:
        return self.Q_(kelvin, 'kelvin').to('degC').magnitude

    def fahrenheitParaKelvin(self, fahrenheit: float) -> float:
        return self.Q_(fahrenheit, 'degF').to('kelvin').magnitude

    def kelvinParaFahrenheit(self, kelvin: float) -> float:
        return self.Q_(kelvin, 'kelvin').to('degF').magnitude

# Exemplo de uso
if __name__ == "__main__":
    conversor = ConversorTemperaturaPadrao()

    # Conversão de Celsius para Fahrenheit
    celsius = 67.0
    fahrenheit = conversor.celsiusParaFahrenheit(celsius)
    print(f"{celsius}°C equivalem a {fahrenheit}°F")

    # Conversão de Fahrenheit para Celsius
    fahrenheit = 88.0
    celsius = conversor.fahrenheitParaCelsius(fahrenheit)
    print(f"{fahrenheit}°F equivalem a {celsius}°C")

    # Conversão de Celsius para Kelvin
    celsius = 34.0
    kelvin = conversor.celsiusParaKelvin(celsius)
    print(f"{celsius}°C equivalem a {kelvin}K")

    # Conversão de Kelvin para Celsius
    kelvin = 546.13
    celsius = conversor.kelvinParaCelsius(kelvin)
    print(f"{kelvin}K equivalem a {celsius}°C")

    # Conversão de Fahrenheit para Kelvin
    fahrenheit = 90.0
    kelvin = conversor.fahrenheitParaKelvin(fahrenheit)
    print(f"{fahrenheit}°F equivalem a {kelvin}K")

    # Conversão de Kelvin para Fahrenheit
    kelvin = 777.77
    fahrenheit = conversor.kelvinParaFahrenheit(kelvin)
    print(f"{kelvin}K equivalem a {fahrenheit}°F")
