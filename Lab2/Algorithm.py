from statistics import mean, stdev
import matplotlib.pyplot as plt
from Individ import Individ
from Population import Population


class Algorithm:
    def __init__(self, problem, data):
        self.problem = problem
        self.data = data
        self.mutProb = None
        self.noGen = None
        self.popSize = None
        self.readParameters("param.in")
        self.population = Population(self.popSize, problem)

    def readParameters(self, fileName):
        f = open(fileName, "r")
        self.mutProb, self.noGen, self.popSize = f.readline().split(" ", 3)
        self.mutProb, self.noGen, self.popSize = float(self.mutProb), int(self.noGen), int(self.popSize)
        f.close()

    def iteration(self):
        # take the 2 best individs. Makes a crossOver, select the best 2 of 3
        individ1, individ2 = self.population.select()
        child = Individ.crossOver(individ1, individ2)
        child.mutate(self.mutProb)
        self.population.add(sorted([individ1, individ2, child], key=lambda x: x.fitness(), reverse=True)[:2][:])

    def run(self):
        # Run iterations. Get fitness of best individ
        for _ in range(0, self.noGen):
            self.iteration()
        return max([i.fitness() for i in self.population.individs])

    def statistics(self, noRuns):
        # Initialize population
        self.population = Population(self.popSize, self.problem)

        # Chose the best fitness from population
        l = [max([i.fitness() for i in self.population.individs])]

        # Makes a list with best fitness for each generation after each iteration
        for _ in range(0, self.noGen):
            self.iteration()
            l.append(max([i.fitness() for i in self.population.individs]))
        plt.plot(l)
        plt.show()
        l.clear()

        # It runs the AI 'noRuns' times
        for i in range(0, noRuns):
            print(str((i / noRuns) * 100) + "%")
            # Refresh the population
            self.population = Population(self.popSize, self.problem)
            # Pick the best
            l.append(self.run())
        print("100% done")
        print("Best solution:", max(l))
        print("Average solution:", mean(l))
        print("Standard deviation:", stdev(l))
