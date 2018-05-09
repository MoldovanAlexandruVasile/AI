from Ant import Ant


class Controller:
    def __init__(self, problem):
        self.problem = problem
        # The number of nodes in the graph
        self.size = problem.noOfCubes * 24

    def initTrace(self, noCubes):
        # Compute the adjacency matrix of the graph
        noRotations = 24
        size = noRotations * noCubes
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(noRotations * noCubes):
            x = i // noRotations
            for j in range(noRotations):
                if x * noRotations - noRotations + j >= 0:
                    matrix[x * noRotations - noRotations + j][i] = 1
        return matrix

    def iteration(self, noAnts, trace, alpha, beta, q0, rho):
        antSet = [Ant(self.problem) for _ in range(noAnts)]
        # the number of iterations of an iteration it's the number of cubes that we have
        for i in range(self.problem.noOfCubes):
            for x in antSet:
                # add a move for each ant we have
                x.addMove(q0, trace, alpha, beta)
        # we update the trace with the fermons left behind by the ants
        dTrace = [1.0 / antSet[i].fitness() for i in range(len(antSet))]
        for i in range(self.size):
            for j in range(self.size):
                trace[i][j] = (1 - rho) * trace[i][j]
        for i in range(len(antSet)):
            for j in range(len(antSet[i].path) - 1):
                x = antSet[i].path[j]
                y = antSet[i].path[j + 1]
                trace[x][y] = trace[x][y] + dTrace[i]
        # return best ant path
        f = [[antSet[i].fitness(), i] for i in range(len(antSet))]
        f = max(f)
        return antSet[f[1]].path

    def run(self, noEpoch, noAnts, alpha, beta, rho, q0):
        bestSol = []
        trace = self.initTrace(self.problem.noOfCubes)
        for i in range(noEpoch):
            print(str((i / noEpoch) * 100) + "%")
            sol = self.iteration(noAnts, trace, alpha, beta, q0, rho).copy()
            if len(sol) > len(bestSol):
                bestSol = sol.copy()
        print("100% ~ DONE")
        print("The length of the best solution is: ", len(bestSol))
