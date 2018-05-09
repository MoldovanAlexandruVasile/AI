from random import *
from Utils import *


class Ant:
    def __init__(self, problem):
        # all the cubes
        self.problem = problem
        # ants path
        self.path = [randint(0, 23)]

    def nextMoves(self):
        # next level of cubes from the graph where the ant can go
        return [range(len(self.path) * 24 + 1, len(self.path) * 24 + 1 + 24)]

    def addMove(self, q0, trace, alpha, beta):
        # add a new position in the solution of the ant
        # the positions that aren't valid will be marked with 0
        p = [0 for _ in range(self.problem.noOfCubes)]
        # in nextStepts will be places the next valid moves
        nextSteps = self.nextMoves()

        # if there are not any posible moves we return false
        if (len(nextSteps) == 0):
            return False

        # compute the product between trace^alpha and visualization^beta
        p = [(p[i] ** beta) * (trace[self.path[-1]][i] ** alpha) for i in range(len(p))]

        # add the best move from all the posible moves
        if (random() < q0):
            p = [[i, p[i]] for i in range(len(p))]
            p = max(p, key=lambda a: a[1])
            self.path.append(p[0])
        else:
            # we add with a probability a posible path
            s = sum(p)
            if (s == 0):
                return choice(nextSteps)
            p = [p[i] / s for i in range(len(p))]
            p = [sum(p[0:i + 1]) for i in range(len(p))]
            r = random()
            i = 0
            while (r > p[i]):
                i = i + 1
            self.path.append(i)
        return True

    def fitness(self):
        # get the actual cubes
        l = []
        for i in self.path:
            l.append(rotate(i % 24, self.problem.problemData[i // 24]))
        # return the side faces
        cubes2 = sorted([remove(i) for i in l])
        maxLen = 0
        currentElem = None
        currentSeqLen = 0
        # Find the longest sequence of cubes
        for elem in cubes2:
            # taking first cube from cubes
            if currentElem is None:
                currentSeqLen += 1
                currentElem = elem
            # verify if the sequence continues
            elif currentElem == elem:
                currentSeqLen += 1
            # start a new sequence
            else:
                maxLen = max(currentSeqLen, maxLen)
                currentSeqLen = 1
                currentElem = elem
        maxLen = max(currentSeqLen, maxLen)
        return maxLen
