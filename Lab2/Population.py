from Individ import Individ


class Population:
    def __init__(self, noIndivids, problem):
        self.noIndivids = noIndivids
        self.individs = [Individ(problem.problemData[:]) for _ in range(0, noIndivids)]

    def select(self):
        self.individs.sort(key=lambda x: x.fitness(), reverse=True)
        return self.individs.pop(0), self.individs.pop(0)

    def add(self, individs):
        self.individs += individs