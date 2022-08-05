# codigo para enviar msgs para pessoas com debito automatico 

class DebitoAutomatico:
    @classmethod
    def debitar(self, conta, valor, banco):
        if banco == "itau":
            # Codigo especifico do Itaú (exemplo)
            # connect_server_udp(itau_line)
            # itau_line.check_system()
            # itau_zig_zag(valor, 'Token 454')
            print("Débito realizado pelo Itau")
        elif banco == "Santander":
            # Codigo especifico do Santander (exemplo)
            # connect_server_tcp(santander_line)
            # santander_line.check_ping()
            # metodo_106(valor)
            print("Santander, Débito efetuado!")
        elif banco == "Bradesco":
            # Codigo especifico do Bradesco (exemplo)
            print("Sucesso!")
        # ... + 150 bancos...
        elif banco == "Caixa":
            # Codigo especifico da Caixa (exemplo)
            print("Efetuado com sucesso, Caixa Agradece!")


DebitoAutomatico.debitar(120, 123, "itau")
DebitoAutomatico.debitar(110, 456, "Santander")
DebitoAutomatico.debitar(120, 789, "Bradesco")


# Como melhorar o código?

# Podemos observar que a classe está enorme, afinal, ela possui muitas responsabilidades já que cada banco possui uma estratégia. Que tal começar criando um Objeto/Classe para cada banco? Como possuem similaridades, é possível respeitar uma interface única — por exemplo, todos possuírem um método debitar().

from abc import ABC, abstractmethod


class BancoStrategy(ABC):  # Interface
    @classmethod
    @abstractmethod
    def debitar(cls):
        raise NotImplementedError


class ItauStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos especifico do Itau (exemplo)
        print("Débito realizado pelo Itau")


class SantanderStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos especifico do Santander (exemplo)
        print("Santander, Débito efetuado!")


class BradescoStrategy(BancoStrategy):
    @classmethod
    def debitar(cls, conta, valor):
        # Codigos especifico do Bradesco (exemplo)
        print("Sucesso!")

# ... métodos para todos os bancos


# As classes foram colocadas juntas no mesmo arquivo como forma de facilitar a visualização. Considere que cada uma já pode estar em seu respectivo arquivo.
# O último passo será criar a classe Banco, que receberá como parâmetro a estratégia escolhida:

from itau_strategy import ItauStrategy
from santander_strategy import SantanderStrategy
from bradesco_strategy import BradescoStrategy

class Banco:
    def __init__(self, banco_strategy):
        self.__banco_strategy = banco_strategy

    def debitar(self, conta, valor):
        self.__banco_strategy.debitar(conta, valor)

Banco(ItauStrategy).debitar(120, 123)
Banco(SantanderStrategy).debitar(110, 456)
Banco(BradescoStrategy).debitar(120, 789)

# Com o padrão Strategy, podemos definir uma família de algoritmos com estrutura similares, encapsulando a lógica de cada estratégia.