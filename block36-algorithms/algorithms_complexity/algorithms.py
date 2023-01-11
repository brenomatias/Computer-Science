def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number

    return sum

#  tempo de execução depende do tamanho do array passado por parâmetro! Quanto maior o tamanho dele, mais tempo o algoritmo gastará em sua execução.


# Suponha que, para o array abaixo, o tempo de execução seja `n`
sum_array(array_com_dez_mil_numeros)

# Nesse caso, aqui o tempo de execução vai ser `10 * n`, ou `10n`, já que o array é dez vezes maior que o anterior
sum_array(array_com_cem_mil_numeros)

# Já esse é dez mil vezes maior que o primeiro, então esse aqui executa em `100n`
sum_array(array_com_um_milhão_de_numeros)


# Note que conforme aumentamos o valor da entrada, o tempo de execução do algoritmo aumenta proporcionalmente, de acordo com uma taxa

# É isso que chamamos de complexidade: A taxa de crescimento do tempo de execução de um algoritmo; quanto maior é essa taxa, maior é seu tempo de execução e, portanto, maior sua complexidade.


# Ordem de Complexidade nada mais é do que a representação dessa proporção (ou taxa) de crescimento


# A partir de agora, sempre que falarmos sobre a Ordem de Complexidade não iremos nos referir ao tempo em segundos que um algoritmo leva para ser executado, mas sim a quantidade de operações que ele realiza. 🙂