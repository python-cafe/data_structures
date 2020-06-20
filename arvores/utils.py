
def graphviz(tree, *args, **kargs):
    def walk(node, depth=0):
        yield (node, depth)
        if node.left:
            for it in walk(node.left, depth + 1):
                yield it
        if node.right:
            for it in walk(node.right, depth + 1):
                yield it


    lines, edges, nodes = ["digraph D {"], [], []
    
    COLORSCHEME_N = 8
    lines.append('\tnode [ colorscheme="pastel28" style="filled"]')

    for node, depth in walk(tree.root):
        depth %= COLORSCHEME_N
        child_depth = (depth + 1) % COLORSCHEME_N
        nodes.append(f'\t"{node.data}" [color="{depth + 1}"];')

        left = f"nl{node.data}"
        if node.left:
            left = node.left.data
        else:
            nodes.append(f'\t"{left}" [label="" color="{child_depth + 1}"];')

        right = f"nr{node.data}"
        if node.right:
            right = node.right.data
        else:
            nodes.append(f'\t"{right}" [label="" color="{child_depth + 1}"];')

        edges.append(f'\t"{node.data}" -> "{left}";')
        edges.append(f'\t"{node.data}" -> "{right}";')

    lines.append("")
    lines.extend(nodes)
    lines.append("")
    lines.extend(edges)

    lines.append("}")
    return '\n'.join(lines)

def save_graphviz(tree, filename):
    filename += ".dot"
    with open(filename, "w") as file:
        file.write(graphviz(tree))
    print("graphviz: " + filename)
