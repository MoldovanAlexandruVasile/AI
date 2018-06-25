import math
import operator


class kNN:
    def __init__(self, k):
        self.k = k

    # Calculate similarity between any two instances
    # Needed to locate the k most similar data instances
    # in the training data set for a given member of the data set
    def euclideanDistance(self, instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    # Compute a weighted distance
    # The weights to nearest neighbors are given
    # by the gaussianDistance function
    def gaussianDistance(self, dist, sigma=1):
        return 1.0 / (math.sqrt(2. * math.pi) * sigma) * math.exp(-dist ** 2 / (2 * sigma ** 2))

    # Here we collect the k most similar instances
    # The function calculate the distance for all instances
    # and selects the subset with the smalles distance value
    # using the euclideanDistance function
    def getNeighbors(self, trainingSet, testInstance):
        distances = []
        length = len(testInstance) - 1
        for x in range(len(trainingSet)):
            dist = self.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(self.k):
            neighbors.append(distances[x])
        return neighbors

    # After locating the most similar neighbors for a test instance
    # we compute a predicted response based on the top k neighbors
    # with biggest similarity
    # Each neighbor will vote for their class attribute
    # For the top K we will compute the gaussianDistance
    # The prediction will be the average of the total neighbor votes
    def getResponse(self, neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
            sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        v = 0
        sum = 0
        predictions = []
        for i in range(self.k):
            if sum != 3:
                sum += sortedVotes[i][1]
                weight = self.gaussianDistance(sortedVotes[i][0])
                v += float(sortedVotes[i][0]) * float(weight)
        predictions.append(v / self.k)
        return predictions
