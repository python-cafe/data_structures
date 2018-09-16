from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        """Insere elem ao final da lista"""
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)
        self._size = self._size + 1

    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        """Retorna o índice de elem na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        return -1

    def __len__(self):
        return self._size

    # def remove(self, elem):
    #     pointer = self.head
    #     if pointer.data == elem: #queremos remover o primeiro elemento
    #         self.head = pointer.next
    #     else:
    #         while(pointer.next):
    #             if pointer.next.data == elem:
    #                 pointer.next = pointer.next.next
lista.append(7)
lista.append(8)
lista.append(9)
