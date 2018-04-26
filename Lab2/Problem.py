class Problem:
    def __init__(self):
        self.problemData = []
        self.noOfCubes = None

    def loadData(self, fileName):
        f = open(fileName, "r")
        totalCubes = f.readline()
        self.noOfCubes = int(totalCubes)
        for line in f:
            c1, c2, c3, c4, c5, c6 = line.split(" ")
            c6 = c6.rstrip("\n")
            self.problemData.append([c1, c2, c3, c4, c5, c6])
        f.close()