# Vamos considerar uma aplicação que gera três tipos de gráficos:
# Para desenvolver esta aplicação, podemos criar uma classe Grafico(), possuindo um método para cada gráfico existente, e um método geral desenhar(), que possui uma condição para escolher o tipo de gráfico

class Grafico:
    def __init__(self, dados):
        self.dados = dados

    def desenhar(self, tipo_de_grafico): # metodo geral
        if tipo_de_grafico == "GraficoBarras":
            self.__desenhar_grafico_barras()

        if tipo_de_grafico == "GraficoRadar":
            self.__desenhar_grafico_radar()

        if tipo_de_grafico == "GraficoPizza":
            self.__desenhar_grafico_pizza()

    def __desenhar_grafico_barras(self): # metodo grafico especifico
        print("Lógica para gráfico de barras")

    def __desenhar_grafico_radar(self): # metodo grafico especifico
        print("Lógica para gráfico radar")

    def __desenhar_grafico_pizza(self): # metodo grafico especifico
        print("Lógica para gráfico de Pizza")


grafico_1 = Grafico([1, 2])
grafico_1.desenhar("GraficoRadar")

# Este código pode parecer seguir as boas práticas de estrutura. Entretanto, sempre que forem adicionados novos gráficos ele ficará ainda maior e consequentemente custoso para realizar a manutenção.