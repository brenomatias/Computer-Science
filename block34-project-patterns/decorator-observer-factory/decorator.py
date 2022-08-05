# daremos mais poderes aos nossos métodos sem a necessidade de subclasses para estender funcionalidades.


# a calculadora para um jogo de matemática para a Educação Infantil:

class Calculadora:
    def soma(self, x, y):
        return x + y

# Porém, recebemos a missão de criar uma calculadora que consiga interpretar números escritos por extenso, reconhecendo em inglês ou em português, dependendo de como a pessoa usuária preferir

class CalculadoraDecorada:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def converterNumero(self, numero):
        if not isinstance(numero, str):
            return numero

        # Neste cenário, em vez de fazermos IF e else... podemos usar o dicionário
        # conseguimos acessar obter o valor a partir da chave
        return {
            "um": 1, "dois": 2, "três": 3, "quatro": 4, "cinco": 5,
            "seis": 6, "sete": 7, "oito": 8, "nove": 9, "dez": 10,
        }.get(numero)

    def soma(self, x, y):
        return self.calculadora.soma(
            self.converterNumero(x), self.converterNumero(y)
        ) 

# Agora que já temos uma calculadora decorada, podemos utilizá-la no lugar da principal:

if __name__ == "__main__":
    calculadora = Calculadora()
    print("10 + 20 =")
    calculadora.soma(10, 20)

calculadoraDecorada = CalculadoraDecorada(calculadora)
print("'oito' + 'dois' =", calculadoraDecorada.soma("oito", "dois"))