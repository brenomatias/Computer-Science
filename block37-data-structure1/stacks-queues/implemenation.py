class Stack():
    def __init__(self):
        self._data = list()

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self.size())

   # funçoes auxiliares

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            return None

        # -1 se refere ao último objeto da pilha.
        # Ou seja, o valor do topo da pilha
        value = self._data[-1]
        del self._data[-1]
        return value

    def peek(self):
        if self.is_empty():
            return None
        value = self._data[-1]
        return value

# clear, que se encarregará de limpar todos os elementos da pilha.
    def clear(self):
        self._data.clear()


#  método __str__ que fará a impressão de todos os elementos que estão empilhados. Do primeiro ao último item inserido (da parte de baixo da pilha até o topo)
    def __str__(self):
        str_items = ""
        for i in range(self.size()):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < self.size():
                str_items += ", "

        return "Stack(" + str_items + ")"

# O método push adiciona um novo valor no topo da pilha, enquanto que o método pop irá pegar o elemento do topo e então retornar esse valor. Nem sempre é interessante remover o valor da pilha, por isso iremos implementar o método peek que somente lê o valor no topo da pilha e então o retorna