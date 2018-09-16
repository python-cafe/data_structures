from node import Node

# inserir na fila
# remover da fila
# observar o primeiro da fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1


    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            # faltou tratar este caso no vídeo #
            if self.first is None:
                self.last = None
            ####################################
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")


    def peek(self):
        # retorna o topo sem remover
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("The queue is empty")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()
