try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")


# Sempre devemos fechar um arquivo e podemos, em um bloco 'try', fazer isso utilizando a instrução 'finally' ou 'else'.

# o 'else' ocorre sempre que todo o 'try' for bem sucedido.