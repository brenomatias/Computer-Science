while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.


# Se ocorrer uma exceção durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas. Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada.


# Se não existir nenhum tratador previsto para tal exceção, trata-se de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.