from node_impl import Node


class LinkedList:
    def __init__(self):
        self.head_value = None
        self.__length = 0

    def __str__(self):
        return f"LinkedList(len={self.__length}, value={self.head_value})"
# Literal String Interpolation na função __str__

    def __len__(self):
        return self.__length