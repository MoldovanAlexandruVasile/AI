from kNN import *


class Controller:
    def __init__(self, fileName,k):
        self.trainData = []
        self.testData = []
        self.readFromFile(fileName)
        self.k = k

    # Reading data from the file.
    def readFromFile(self, fileName):
        f = open(fileName)
        sem = False
        while sem == False:
            line = f.readline()
            if line != "":
                line = line.split(',')
                self.trainData.append([float(nr) for nr in line[0:7]])
                self.testData.append([float(nr) for nr in line[7:]])
            else:
                sem = True

    # Check the accuracy of the predictions
    def getAccuracy(self, testSet, predictions):
        correct = 0
        for x in range(len(testSet)):
            if predictions[x] in testSet[x]:
                correct += 1
        return float(correct) / float(len(testSet)) * 100

    def run(self):
        knn = kNN(self.k)
        # generate predictions
        predictions = []
        for x in range(len(self.testData)):
            neighbors = knn.getNeighbors(self.trainData, self.testData[x])
            predicted = knn.getResponse(neighbors)[-1]
            predicted = float('%.2f' % predicted)
            predictions.append(predicted)
        accuracy = self.getAccuracy(self.testData, predictions)
        result = float('%.2f' % accuracy)
        print('\n\tAccuracy is: ' + repr(result) + '%')
