# Eles significam o seguinte: "A depender da minha entrada, o meu algoritmo pode executar em O(1) ou O(n)". Por exemplo, pense na busca sequencial:

def linear_search(numbers, target):
    n = len(numbers) # N será a quantidade de elementos da lista
    for index in range(0, n): # vamos iterar a lista completa
        if numbers[index] == target: # se encontrar o elemento alvo, retorne a posição
            return index

    return -1 # Não encontrou? Retorne -1


print(linear_search([1, 2, 3], 2))  # saída: 1
print(linear_search([1, 2, 3], 4))  # saída: -1