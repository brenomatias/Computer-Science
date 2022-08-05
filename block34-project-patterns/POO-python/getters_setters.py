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


liquidificador = Liquidificador("Azul", "110", "127", "200")

# print(f"A cor atual é {liquidificador.__cor}")
# AttributeError: 'Liquidificador' object has no attribute '__cor'

print(f"A cor atual é {liquidificador.cor}")
liquidificador.cor = "Vermelho" # acessa a cor e da um set por causa dos metodos
print(f"Após pintarmos, a nova cor é {liquidificador.cor}")