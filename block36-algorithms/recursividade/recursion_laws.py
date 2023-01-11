def countdown(n):
    print(n)
    countdown(n - 1)  # chamada recursiva

countdown(5)

# Observe que dentro da implementação desta solução, a função chama ela mesma.

# Isso é uma chamada recursiva! Lembre-se que a recursão é quando uma função chama ela mesma. Se você executar esse código, ele ficará em loop infinito!



# Quando estamos escrevendo uma função recursiva, precisamos informar nossa condição de parada ou caso base da recursão. Nesse sentido, podemos separar uma função recursiva em:
#  * Caso base e Caso recursivo

# código sem loop infinito
def countdown(n):
    if n == 0: # caso base
        print("FIM!")
    else:
        print(n)
        countdown(n - 1) # caso recursivo

countdown(5)



def factorial(n):
    if n == 1: # caso base
        return 1
    else:
        return n * factorial(n - 1) # caso recursivo