def is_odd(number):
    'Retorna True se um número é ímpar, senão False.'
    result = number % 2 != 0

    return result

print('The answers is', is_odd(3))