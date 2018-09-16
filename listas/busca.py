# Busca linear em lista em alocação sequencial

def busca(lista, elem):
    """Retorna o índice elem se ele estiver na lista ou None, caso contrário"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = "python"

indice = busca(lista_estranha, elemento)
if indice is not None:
    print("O índice do elemento {} é {}".format(elemento, indice))
else:
    print("O elemento {} não se encontra na lista".format(elemento))
