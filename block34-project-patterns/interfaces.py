# precisamos criar uma classe que será a Interface, responsável por definir os combinados para suas classes herdeiras.

from abc import ABC, abstractmethod 
# classe ABC do Python (Abstract Base Classes)
# Esta herança já avisa o Python para ele entender que este código não terá a implementação concreta de um Gráfico.

class Grafico(ABC):
    @abstractmethod
    def desenhar(self):
        raise NotImplementedError

# nossa classe Interface será a Grafico, sua única responsabilidade será declarar a assinatura dos métodos de um gráfico. Assim conseguimos forçar que suas herdeiras sigam o mesmo padrão (como respeitar um contrato).

class GraficoBarras(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Lógica para gráfico de barras")


class GraficoRadar(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Lógica para gráfico radar")


class GraficoPizza(Grafico):
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self):
        print("Lógica para gráfico de Pizza")


grafico_1 = GraficoRadar([1, 2])
grafico_1.desenhar()