#!/usr/bin/python
import copy

from tree import Node

"""
    8-Puzzle problem solved with methods: Manhatan, Tiles and blind Search - for AI discipline
    Gustavo Cardozo Rodrigues - 151151360
    Universidade Federal do Pampa - Alegrete/RS  
"""

# inicial = [3, 2, 1, 0, 4, 5, 6, 8, 7]
# inicial = [7, 2, 4, 5, 0, 6, 8, 3, 1]
inicial = [1, 6, 7, 2, 5, 3, 4, 0, 8]

final = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

dicionario = {}
exp = 0 # Contador de expansoes


def getKey(node):
    return node.cost


def expandNode(node, h, g):
    """
    :param node: node a ser expandido
    :param h: funcao de heuristica
    :param g: funcao g
    :return: retorna uma lista contendo os filhos do node expandido
    """
    expNode = [] # contem os nos filhos
    possibleExp = []  # locais para onde pode expandir
    possibleExp.extend(node.getPossibleMoves())

    global exp
    global dicionario

    for move in possibleExp:
        """
            Testa cada posicao criando um node auxiliar para cada posicao possivel
            Se o estado criado ainda nao foi explorado, este eh adicionado na lista expNode
        """
        # g(node) + h(node)
        if move == "up":
            son = Node(node.up(), node, move, node.depth + 1, h(node) + g(node))
            if not son.isOnDic(dicionario):
                son.addOnDic(dicionario)
                expNode.append(son)
                exp += 1
        elif move == "down":
            son = Node(node.down(), node, move, node.depth + 1, h(node) + g(node))
            if not son.isOnDic(dicionario):
                son.addOnDic(dicionario)
                expNode.append(son)
                exp += 1
        elif move == "left":
            son = Node(node.left(), node, move, node.depth + 1, h(node) + g(node))
            if not son.isOnDic(dicionario):
                son.addOnDic(dicionario)
                expNode.append(son)
                exp += 1
        elif move == "right":
            son = Node(node.right(), node, move, node.depth + 1, h(node) + g(node))
            if not son.isOnDic(dicionario):
                son.addOnDic(dicionario)
                expNode.append(son)
                exp += 1

    return expNode


def solve(h, g):
    """
    :param h: funcao heuristica - Manhatan, tiles ou blind
    :param g: funcao g para A* - Depht
    :return: retorna uma lista contendo os movimentos feitos ate a resolucao

    """
    print ("Resolvendo...")
    fila = []  # Fila de prioridade para expansao
    min = Node(inicial, None, None, 0, 0)  # primeiro elemento da lista
    min.cost = h(min) + g(min)  # calculo do custo do elemento
    fila.append(min)  # primeiro elemento na lista
    global dicionario
    global dicionarioExp

    while True:
        if len(fila) == 0: return None

        if (min.cost != 0): fila = sorted(fila, key=getKey)  # Ordena a lista conforme o custo

        node = fila.pop(0)  # Pega o primeiro elemento da lista para expandilo

        if node.state == final:  # se o estado que foi pego for igual ao final entao foi resolvido
            moves = []  # Lista para armazenar os movimentos
            aux = copy.deepcopy(node)  # Auxiliar recebe o ultimo no

            while not aux.depth == 0:
                # insere a operacao q gerou
                moves.append(aux.operator)
                if aux.depth == 0:
                    break
                if aux.parent:
                    aux = aux.parent
            return moves

        # expande o no e adiciona as aberturas dele na fila
        # estados repetidos nao sao armazenados
        fila.extend(expandNode(node, h, g))


def g_blind(node):
    return 0


def g_depth(node):
    """
    :param node: recebe um no
    :return: retorna a profundidade do no + 1
    """
    return node.depth + 1


def h_blind(node):
    return 0


def h_manhattan(node):
    """
    :param node:
    :return: retorna o somatorio da diferenca da
            localizacao atual para a localizacao desejada de cada numero
    """
    t = 0
    for i in range(len(node.state)):
        t += abs(node.state[i] - (i % 9))
    return t


def h_tiles(node):
    """
    :param node:
    :return: retorna quantos numeros estao fora de posicao
    """
    t = 0
    for i in range(len(node.state)):
        if not (node.state[i] == i):
            t += 1

    return t


def main():
    moves = solve(h_manhattan, g_depth)  # chamada da funcao para resolucao do problema
    if moves == None:
        print ("solucao n encontrada")
        return

    result = Node(inicial, None, 'a', 0, 0)
    result.showState()
    moves.reverse()
    # Reconstroi os nos para printar o caminho ate a resolucao do problema
    for next in moves:
        print(next)
        if next == "up":
            result.state = result.up()
        elif next == "down":
            result.state = result.down()
        elif next == "left":
            result.state = result.left()
        elif next == "right":
            result.state = result.right()

        result.showState()

    print (moves)
    print (str(len(moves)) + " movimentos")
    print (str(exp) + " expansoes")
    print ("Feito!")


if __name__ == "__main__":
    main()
