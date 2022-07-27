import csv

with open("graduacao_unb.csv", encoding = "utf-8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

print(data)

# O leitor define como dialeto padrão excel, o que significa dizer que o delimitador de campos será ","

#  o caractere de citação será aspas duplas (") "quotechar"

# lém disso, o leitor irá usar o decodificador padrão do sistema para decodificar em unicode o arquivo - "encoding"

# Um leitor de .csv pode ser percorrido utilizando o laço de repetição for e, a cada iteração, retorna uma nova linha já transformada em uma lista Python com seus respectivos valores.