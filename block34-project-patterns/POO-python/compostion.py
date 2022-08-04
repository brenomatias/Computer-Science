class Liquidificador:
    def __init__(self, cor, potencia, voltagem, preco):
        self.preco = preco
        self.__cor = cor
        self.__potencia = potencia
        self.__voltagem = voltagem
        self.__ligado = False
        self.__amperagem_atual_no_motor = 0

    # Getter
    @property
    def cor(self):
        return self.__cor
# criar um método com o nome do atributo 'cor' e decorar ele com o @property para facilitar o acesso de fora 'liquidificador.cor'

    # Setter
    @cor.setter
    def cor(self, nova_cor):
        self.__cor = nova_cor


class Pessoa: # nova classe
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def comprar_liquidificador(self, liquidificador: Liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador
# Liquidificador -> a classe do liquidificador

    def __str__(self):
        return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."
        # printar o resultado de maneira personalizada


pessoa_cozinheira = Pessoa("Jacquin", 1000)
pessoa_cozinheira.comprar_liquidificador(liquidificador_vermelho)


print(pessoa_cozinheira)
# retorno: Pessoa object at 0x7f53bbe1b580> 
# ao imprimir a instância de um objeto, o Python exibe a posição de memória do objeto.

# Uma forma de melhorar esta apresentação, é implementar o método "__str__" para a classe que deseja imprimir

    #     def __str__(self):
    #     return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."
