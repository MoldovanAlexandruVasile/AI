from Network import *
from math import sqrt

moves = {"Sharp-Right-Turn": 1, "Slight-Right-Turn": 2, "Move-Forward": 3, "Slight-Left-Turn": 4}


class Controller:
    def __init__(self, noTE, noF, noO, noTstE):
        self.noTrainExamples = noTE
        self.noFeatures = noF
        self.noOutputs = noO
        self.inTrainData = []
        self.outTrainData = []

        self.noTestExamples = noTstE
        self.inTestData = []
        self.outTestData = []

        self.readData(self.noTrainExamples, self.inTrainData, self.outTrainData, "data.txt")
        self.readData(self.noTestExamples, self.inTestData, self.outTestData,
                      "E:\\Programe\\Python\\Programe\\IA\\Lab4\\dataTesting.txt")

    def readData(self, noExamples, inData, outData, fileName):
        f = open(fileName)
        for i in range(noExamples):
            line = f.readline()
            if line != "":
                line = line.split(',')
                outData.append(moves[line[len(line) - 1].strip()])
                inData.append([float(nr) for nr in line[:len(line) - 1]])

    def normaliseData(self, noExamples, noFeatures, trainData, noTestExamples, testData):
        # statistical normalisation
        for j in range(noFeatures):
            summ = 0.0
            for i in range(noExamples):
                summ += trainData[i][j]
            # Make the average
            mean = summ / noExamples
            squareSum = 0.0
            for i in range(noExamples):
                squareSum += (trainData[i][j] - mean) ** 2
            # Compute the deviation
            deviation = sqrt(squareSum / noExamples)
            # Assign the new values
            for i in range(noExamples):
                trainData[i][j] = (trainData[i][j] - mean) / deviation
            for i in range(noTestExamples):
                testData[i][j] = (testData[i][j] - mean) / deviation

    def run(self):
        self.normaliseData(self.noTrainExamples, self.noFeatures, self.inTrainData, self.noTestExamples,
                           self.inTestData)

        net = Network(self.noFeatures, self.noOutputs, 1, 2)

        net.learning(self.inTrainData, self.outTrainData)
        net.testing(self.inTestData, self.outTestData)
