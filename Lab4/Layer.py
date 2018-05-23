from Neuron import *


class Layer:
    def __init__(self, noN, noIn):
        self.noNeurons = noN
        self.neurons = [Neuron(noIn) for _ in range(self.noNeurons)]
