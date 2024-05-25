'''

4. Interface ConversorTemperatura:
Define os métodos:
celsiusParaFahrenheit(double celsius) para converter Celsius para
Fahrenheit.
fahrenheitParaCelsius(double fahrenheit) para converter Fahrenheit para
Celsius.

'''

from abc import ABC, abstractmethod

class ConversorTemperatura(ABC):
    @abstractmethod
    def celsiusParaFahrenheit(self, celsius: float) -> float:
        pass

    @abstractmethod
    def fahrenheitParaCelsius(self, fahrenheit: float) -> float:
        pass

class ConversorTemperaturaImpl(ConversorTemperatura):
    def celsiusParaFahrenheit(self, celsius: float) -> float:
        return (celsius * 9/5) + 32

    def fahrenheitParaCelsius(self, fahrenheit: float) -> float:
        return (fahrenheit - 32) * 5/9

# Exemplo de uso
if __name__ == "__main__":
    conversor = ConversorTemperaturaImpl()
    
    celsius = 56.0
    fahrenheit = conversor.celsiusParaFahrenheit(celsius)
    print(f"{celsius}°C equivalem a {fahrenheit}°F")

    fahrenheit = 100.0
    celsius = conversor.fahrenheitParaCelsius(fahrenheit)
    print(f"{fahrenheit}°F equivalem a {celsius}°C")

