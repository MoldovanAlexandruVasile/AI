from Layer import *


class Network:
    def __init__(self, m, r, p, h):
        self.noInputs = m
        self.noOutputs = r
        self.noHiddenLayers = p
        self.noNeuronsPerHiddenLayer = h
        self.layers = [Layer(self.noInputs, 0)]
        self.layers += [Layer(self.noNeuronsPerHiddenLayer, self.noInputs)]
        self.layers += [Layer(self.noNeuronsPerHiddenLayer,
                              self.noNeuronsPerHiddenLayer) for _ in range(self.noHiddenLayers - 1)]
        self.layers += [Layer(self.noOutputs, self.noNeuronsPerHiddenLayer)]

        self.LEARN_RATE = 0.1
        self.EPOCH_LIMIT = 1000

    def activate(self, inputs):
        # Assign each neuron an input value
        # then each neuron will be activated
        i = 0
        # for n in self.layers[0]:
        for n in self.layers[0].neurons:
            n.output = inputs[i]
            i += 1

        # for l in range(1, self.noHiddenLayers + 1):
        for l in range(0, self.noHiddenLayers + 2):
            # for n in self.layers[l]:
            for n in self.layers[l].neurons:
                info = []
                # Take each neurons output and place it in a list
                for i in range(n.noInputs):
                    info.append(self.layers[l - 1].neurons[i].output)
                # Then the current neuron will be activated
                n.activate(info)

    def errorsBackPropagate(self, err):
        # for l in range(self.noHiddenLayers + 1, 1, -1):
        for l in range(self.noHiddenLayers + 1, 0, -1):
            i = 0
            # for n1 in self.layers[l]:
            for n1 in self.layers[l].neurons:
                if (l == self.noHiddenLayers + 1):
                    n1.setErr(err[i])
                else:
                    sumErr = 0.0
                    # for n2 in self.layers[l + 1]:
                    for n2 in self.layers[l + 1].neurons:
                        sumErr += n2.weights[i] * n2.err
                    n1.setErr(sumErr)
                for j in range(n1.noInputs):
                    n1.weights[j] = n1.weights[j] + self.LEARN_RATE * n1.err * self.layers[l - 1].neurons[j].output
                i += 1

    def checkGlobalErr(self, err):
        # If the average of the global errors it's bigger
        # than 0.95 we return true and the learning will stop
        # otherwise, it will continue
        correct = sum(err)
        error = correct / len(err)
        if error > 0.95:
            return True
        else:
            return False

    def errorComputationClassification(self, target):
        # normalise the output of neurons from the output layer (softmax transformation;
        # sum of transformed outputs is 1, each transformed output behaves like a probability)
        transfOutputs = []
        maxx = self.layers[self.noHiddenLayers + 1].neurons[0].output
        # We find the maximum output from the neurons
        for i in range(0, self.noOutputs):
            if (self.layers[self.noHiddenLayers + 1].neurons[i].output >= maxx):
                # If we found a bigger output data then we change the max
                maxx = self.layers[self.noHiddenLayers + 1].neurons[i].output
        # We compute the exponential sum of the outputs
        # each of it is decreased by the maximum output that has been found
        sumExp = 0.0
        for i in range(0, self.noOutputs):
            sumExp += exp(self.layers[self.noHiddenLayers + 1].neurons[i].output - maxx)
        # Here the softmax transformation it's computed
        # (normalise each neurons output)
        for i in range(0, self.noOutputs):
            transfOutputs.append(exp(self.layers[self.noHiddenLayers + 1].neurons[i].output - maxx) / sumExp)
        # The predicted answer it's computed
        computedLabel = 1
        for i in range(0, self.noOutputs):
            if (transfOutputs[i] > maxx):
                maxx = transfOutputs[i]
                computedLabel = i + 1
        # If the prediction was succesfull will return 0, otherwise will return 1
        if (target == computedLabel):
            # if the predicted answer is correct
            return 0
        else:
            # if the predicted answer is incorrect
            return 1

    def learning(self, inData, outData):
        # Set a stop condition
        stopCondition = False
        # No of epochs runned
        epoch = 0
        globalErr = []
        while not stopCondition and (epoch < self.EPOCH_LIMIT):
            globalErr = []
            # for each training data
            for i in range(len(inData)):
                self.activate(inData[i])
                # activate all the neurons; propagate forward the signal
                globalErr.append(self.errorComputationClassification(outData[i]))
                # backpropagate the error of neurons
                self.errorsBackPropagate(globalErr)
            # Modify the stop contidion. If changed "True" then stop
            stopCondition = self.checkGlobalErr(globalErr)
            # Go to the next epoch
            epoch += 1
            print(str(epoch / self.EPOCH_LIMIT * 100) + "%")
        print("Learning: " + str(globalErr))

    def testing(self, inData, outData):
        globalErr = []
        # for each testing example
        for i in range(len(inData)):
            # activate all the neurons; propagate forward the signal
            self.activate(inData[i])
            globalErr.append(self.errorComputationClassification(outData[i]))
        print("Testing: " + str(globalErr))
