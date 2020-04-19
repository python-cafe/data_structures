# Programação Dinâmica - Estruturas de Dados
# Implementação de uma árvore binária e percursos na árvore

from queue import Queue


ROOT = "root"
# Vídeo Implementando uma árvore binária: https://youtu.be/6E169kShoNU
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

    # Vídeo "Percurso em Nível em Árvore Binária": 
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

# Vídeo "Árvore Binária de Busca": https://youtu.be/rviJVdt_icw
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
    
    # def search(self, value, node=0):
    #     if node == 0:
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

        