import graphviz
from examples import inorder_example_tree
from test import random_tree


def preorder_traversal(tree, dot):
    # visita a raiz
    dot.node(str(tree.data), str(tree.data))
    if tree.left:
        preorder_traversal(tree.left, dot)
        dot.edge(str(tree.data), str(tree.left.data))
    if tree.right:
        preorder_traversal(tree.right, dot)
        dot.edge(str(tree.data), str(tree.right.data))

def make_viz(tree, name):
    dot = graphviz.Digraph(comment=name)
    preorder_traversal(tree.root, dot)
    dot.render(f'viz/{name}.gv', view=True).replace('\\', '/')

if __name__ == '__main__':
    # tree = inorder_example_tree()
    # make_viz(tree, "expressao")
    tree = random_tree(16)
    make_viz(tree, "aleatoria")