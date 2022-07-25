characters_file = open("Meus personagens.txt", mode='w')

# criar arquivo -> função 'open()'
# mode -> como voce vai interagir (ler, editar, etc)


characters_file.write('Tio Louco\n')
characters_file.write('Foda-se\n')
characters_file.write('Novo personagem\n')

# Adicionar personagens -> escrever em arquivos


print('Batman', file=characters_file)

# da output na saida padrão do sistema que é o terminal, mas se especificar arquivo 'printa' a saída no arquivo


more_characters = ['Lala\n', 'Ash\n']

characters_file.writelines(more_characters)

# pega todos elementos de uma lista e escreve todos no arquivo
# '\n' -> quebra de linha 


characters_file.close()

#fechar arquivo - MUITO IMPORTANTE 
# se nao fechar arquivo o sistema operacional entende que o arquivo ainda esta aberto