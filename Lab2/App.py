from Problem import Problem
from Algorithm import Algorithm
# from Individ import *

class App:
    @staticmethod
    def main():
        p = Problem()
        p.loadData("data.in")
        a = Algorithm(p, [])
        a.statistics(30)


# p = Problem()
# p.loadData("data.in")
# for i in range(20):
#    print(Individ.rotateCube(p.problemData,6))

App.main()
