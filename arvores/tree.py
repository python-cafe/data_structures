# Programação Dinâmica - Estruturas de Dados
# Implementação de Árvores e seus algoritmos - by hallpaz
# https://youtube.com/programacaodinamica

from queue import Queue


ROOT = "root"
# Implementando uma Árvore Binária: https://youtu.be/6E169kShoNU
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso em ordem simétrica (o correto é "inorder" em inglês)
    def simetric_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            # parênteses são específicos para o nosso exemplo,
            # um percurso em ordem simétrica não precisa deles
            print('(', end='') 
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(')', end='')
    
    # Percurso em PÓS ORDEM em ÁRVORE BINÁRIA: https://youtu.be/QC8oiQnlYos
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end=' ')
        if node.right:
            self.inorder_traversal(node.right)

    # Percurso em Nível em Árvore Binária: https://youtu.be/UOK7nS2E9xM
    def levelorder_traversal(self, node=ROOT):
        if node == ROOT:
            node = self.root

        queue = Queue()
        queue.push(node)
        while len(queue):
            node = queue.pop()
            if node.left:
                queue.push(node.left)
            if node.right:
                queue.push(node.right)
            print(node, end=" ")

# Árvore Binária de Busca: https://youtu.be/rviJVdt_icw
class BinarySearchTree(BinaryTree):
    
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)

    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self._search(value, node.left)
        return self._search(value, node.right)

    # Encontrando o MAIOR e o MENOR elemento numa ÁRVORE Binária de Busca: https://youtu.be/Q9s_XyJpHTI
    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root
        while node.right:
            node = node.right
        return node.data

    # REMOVENDO da Árvore Binária de Busca: https://youtu.be/dyLwOXBA3Ws
    def remove(self, value, node=ROOT):
        # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
            node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if value < node.data:
            node.left = self.remove(value, node.left)
        # Se o valor for maior, desce à direita
        elif value > node.data:
            node.right = self.remove(value, node.right)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substitute
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substitute, node.right)

        return node
        
    
    # def search(self, value, node=ROOT):
    #     if node == ROOT:
    #         node = self.root
    #     if node is None or node.data == value:
    #         return BinarySearchTree(node)
    #     if value < node.data:
    #         return self.search(value, node.left)
    #     return self.search(value, node.right)
        
        

if __name__ == "__main__":
    tree = BinaryTree(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)

        