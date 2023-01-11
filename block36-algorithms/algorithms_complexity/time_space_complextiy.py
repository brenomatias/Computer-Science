# dissemos que a complexidade de um algoritmo representa o crescimento de seu tempo de execução em função de uma taxa, a quantidade de operações que ele realiza. Porém, quando falamos em complexidade, não analisamos apenas o tempo, analisamos também o espaço gasto


def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares


# se houver 10 números na entrada de dados,por exemplo, serão realizadas 10 operações; se houver 100 serão realizadas 100 operações. O que isso representa em termos de complexidade?


# Em relação à Complexidade de Tempo, temos aqui uma taxa de crescimento linear, uma vez que o aumento no tamanho do array faz crescer proporcionalmente o tempo gasto na execução do algoritmo


# esse algoritmo vai sempre nos retornar um array com o mesmo tamanho da entrada de dados, pois ele sempre devolve um novo arraycom todos os números de entrada ao quadrado

# Desse modo, conforme a entrada cresce, a saída também cresce e, consequentemente, o espaço ocupado por ela, o que implica dizer que sua Complexidade de Espaço é dada por O(n).