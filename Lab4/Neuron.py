from random import *
from math import exp


class Neuron:
    def __init__(self, noInputs):
        self.noInputs = noInputs
        self.weights = [(random() * 2 - 1) for _ in range(self.noInputs)]
        self.output = 0
        self.err = 0

    def activate(self, info):
        # info is a list of neurons output
        # Compute the new output data of the neuron
        net = 0.0
        for i in range(self.noInputs):
            net += info[i] * self.weights[i]
        # sigmoidal activation
        self.output = 1 / (1.0 + exp(-net))

    def setErr(self, val):
        # Compute each neurons error
        # sigmoidal activation
        self.err = self.output * (1 - self.output) * val
