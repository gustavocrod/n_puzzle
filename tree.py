
class Node:
    def __init__(self, state, parent, operator, depth, cost):
        #custo para busca com alguma heuristica
        self.cost = cost
        #contem o noh que gerou esse no (eh o pai)
        self.parent = parent
        #contem a operacao (lado) que gerou esse noh apartir do pai
        self.operator = operator
        #contem a profundidade deste no
        self.depth = depth
        #contem o estado do no
        self.state = state

    def isOnDic(self, dic):
        """
        :param dic: recebe um dicionario para testar
        :return: retorna true se o estado esta no dicionario, ou seja, se o estado ja foi visitado
        """
        if (str(self.state) in dic):
            return True

        return False

    def addOnDic(self, dic):
        dic[str(self.state)] = True

    def showState(self):
        print ("-------------")
        print ("| %i | %i | %i |" % (self.state[0], self.state[1], self.state[2]))
        print ("-------------")
        print ("| %i | %i | %i |" % (self.state[3], self.state[4], self.state[5]))
        print ("-------------")
        print ("| %i | %i | %i |" % (self.state[6], self.state[7], self.state[8]))
        print ("-------------")
        print ('\n')

    def getPossibleMoves(self):
        """
        :return: retorna uma lista dos possiveis movimentos que podem ser realizados
        (locais onde nao saia fora do range da "matriz"
        """
        zero = self.state.index(0)
        moves = []
        if zero not in [0, 3, 6]:
            moves.append("left")
        if zero not in [2, 5, 8]:
            moves.append("right")
        if zero not in [0, 1, 2]:
            moves.append("up")
        if zero not in [6, 7, 8]:
            moves.append("down")

        return moves


    def left(self):
        newState = list(self.state)
        #procura onde esta localizado o blank

        index = newState.index(0)

        aux = newState[index - 1]
        newState[index - 1] = newState[index]
        newState[index] = aux
        return newState


    def right(self):
        newState = list(self.state)
        # procura onde esta localizado o blank
        index = newState.index(0)

        aux = newState[index + 1]
        newState[index + 1] = newState[index]
        newState[index] = aux
        return newState

    def up(self):
        newState = list(self.state)
        # procura onde esta localizado o blank
        index = newState.index(0)

        aux = newState[index - 3]
        newState[index - 3] = newState[index]
        newState[index] = aux
        return newState

    def down(self):
        newState = list(self.state)
        # procura onde esta localizado o blank
        index = newState.index(0)

        aux = newState[index + 3]
        newState[index + 3] = newState[index]
        newState[index] = aux
        return newState
