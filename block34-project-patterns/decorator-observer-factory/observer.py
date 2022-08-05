# Vamos implementar a representação de um sistema de notificação de uma rede social, de modo que, quando uma pessoa realizar uma nova postagem em seu perfil, todos as pessoas que a seguem serão notificadas. Entretanto, as pessoas seguidoras podem decidir se querem ser notificadas por mensagem, push notification ou e-mail.

class Perfil:
    def __init__(self):
        self.__sistemas_de_notificacao = []  # sistemas de notificações / msg, push, email
        self.__new_post = None

    def adicionar_sistema_de_notificacao(self, sistema): # permitirá que o cadastro de novos sistemas seja feito de forma dinâmica
        self.__sistemas_de_notificacao.append(sistema)

    def notificar_todos(self):
        for sistema in self.__sistemas_de_notificacao:
            sistema.notificar()

    def adicionar_post(self, post): # adicionar um novo post 
        self.__new_post = post
        self.mostrar_post() # exibir post
        self.notificar_todos() # notificará todas as pessoas seguidoras

    def mostrar_post(self):
        print(f"\nPost: {self.__new_post}\n")
        



# Para implementar o padrão Observer, precisaremos criar as classes observadoras que acompanharão o objeto 'Perfil', observando se ele ganha um novo Post. Quando verdadeiro, cada observador vai disparar as notificações.

# Para implementar o padrão Observer, precisaremos criar as classes observadoras que acompanharão o objeto Perfil,

# Criaremos uma classe Observador para cada sistema de envio (E-mail, PushNotification, Mensagem).


from abc import ABC, abstractmethod

# Interface Observer
class Notificador(ABC):
    @abstractmethod
    def notificar(self):
        pass

# Observador Mensagem
class NotificadorMensagem(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Notificando via Mensagens: {self.seguidores}")

# Observador Push Notification
class NotificadorPushNotification(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Disparando Push Notification para: {self.seguidores}")

# Observador Email
class NotificadorEmail(Notificador):
    def __init__(self, perfil, seguidores):
        self.perfil = perfil
        self.seguidores = seguidores
        self.perfil.adicionar_sistema_de_notificacao(self)

    def notificar(self):
        print(f"Disparando Email's para: {self.seguidores}")



# Pronto, agora podemos usar nosso código com o padrão Observer! O código que vamos utilizar é conhecido na literatura como código Cliente:

# Cliente
if __name__ == "__main__":
    seguidores_mensagem = ["Carlos", "Claudia", "Marcia", "Rodolfo"]
    seguidores_push_notification = ["Carlos"]
    seguidores_email = ["Claudia", "Marcia"]

    meuPerfil = Perfil()
    NotificadorMensagem(meuPerfil, seguidores_mensagem)
    NotificadorPushNotification(meuPerfil, seguidores_push_notification)
    NotificadorEmail(meuPerfil, seguidores_email)

    meuPerfil.adicionar_post("Olá universo da programação!")

# Podemos perceber que apenas o uso de meuPerfil.adicionar_post() é suficiente para realizar as notificações. Inclusive ainda podemos notificar as pessoas seguidoras a qualquer momento chamando diretamente meuPerfil.notificar_todos(). Isso é interessante, pois podemos ativar/desativar as formas de notificação apenas alterando um bloco parcial de código, sem precisar alterar o método notificar_todos(). Esta facilidade é conhecida como baixo acoplamento e facilita muito as manutenções futuras.