from Controller import Controller
from Problem import *

if __name__ == "__main__":
    ALPHA = 1.9
    BETA = 0.9
    RHO = 0.05
    Q0 = 0.5
    popSize = 10
    noEpoch = 100

    problem = Problem()
    problem.loadData("data.in")



    print("Program started !")
    ctrl = Controller(problem)
    ctrl.run(noEpoch, popSize, ALPHA, BETA, RHO, Q0)