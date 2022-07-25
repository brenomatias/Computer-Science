PI = 3.14  # PI é uma "constante" em nosso módulo


def square(side):
    '''Calculate area of square.'''
    return side * side


def rectangle(length, width):
    '''Calculate area of rectangle.'''
    return length * width


def circle(radius):
    '''Calculate area of circle.'''
    return PI * radius * radius


# Observe que esse código segue algumas boas práticas para legibilidade, tais como:
# Entre cada função temos um espaço de 2 linhas;
# As funções são declaradas com nomes em letras minúsculas;
# A constante PI é definida em letras maiúsculas.
# ⚠️Aviso: Existe uma convenção de declarar valores considerados constantes com letras maiúsculas, e o respeito por outros programadores de não alterarem aquele valor.


#  Neste módulo só temos definições das funções e valores, mas não estamos executando nenhuma delas. Isto é o que chamamos de execução do módulo como script.


# Hora de testá-lo! 
if __name__ == "__main__":
    print("Área do quadrado:", square(10))
    print("Área do retângulo:", rectangle(2, 2))
    print("Área do círculo:", circle(3))


# ***** if __name__ == "__main__":
# acrescentar uma condicional ao módulo para somente exibir esses valores de teste quando o módulo for executado como script.

# sem isso Os nossos valores de teste estão sendo exibidos quando importamos o módulo em 'people.py'