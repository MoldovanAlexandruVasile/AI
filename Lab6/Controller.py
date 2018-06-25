class Controller:
    def __init__(self, fuz, tempFileName, capFileName, powFileName, funcFileName):
        self.defuzi = 0
        self.fuz = fuz
        self.fuzzyCapacity = self.readCapacity(capFileName)
        self.fuzzyTemperature = self.readTemperatura(tempFileName)
        self.fuzzyPower = self.readPower(powFileName)
        self.functionalityRules = self.readFunctionality(funcFileName)
        self.result = {'small': [], 'medium': [], 'high': []}

    def readTemperatura(self, fileName):
        myMap = {}
        f = open(fileName)
        sem = False
        while sem == False:
            line = f.readline()
            if line != "":
                myTuple = ()
                line = line.split(',')
                for i in range(1, len(line)):
                    myTuple += (int(line[i]),)
                myMap[str(line[0])] = myTuple
            else:
                sem = True
        return myMap

    def readCapacity(self, fileName):
        myMap = {}
        f = open(fileName)
        sem = False
        while sem == False:
            line = f.readline()
            if line != "":
                myTuple = ()
                line = line.split(',')
                for i in range(1, len(line)):
                    myTuple += (int(line[i]),)
                myMap[str(line[0])] = myTuple
            else:
                sem = True
        return myMap

    def readPower(self, fileName):
        myMap = {}
        f = open(fileName)
        sem = False
        while sem == False:
            line = f.readline()
            if line != "":
                myTuple = ()
                line = line.split(',')
                for i in range(1, len(line)):
                    myTuple += (int(line[i]),)
                myMap[str(line[0])] = myTuple
            else:
                sem = True
        return myMap

    def readFunctionality(self, fileName):
        myMap = {}
        myList = []
        f = open(fileName)
        sem = False
        while sem == False:
            line = f.readline()
            if line != "":
                line = line.split(',')
                for i in range(1, len(line), 2):
                    myTuple = (str(line[i]).rstrip(), str(line[i + 1]).rstrip())
                    myList.append(myTuple)
                myMap[str(line[0])] = myList
            else:
                sem = True
        return myMap

    def drange(self, start, stop, step):
        r = start
        while r < stop:
            yield int(r * 10 ** 2) / 10.0 ** 2
            r += step

    def run(self, temperature, capacity):
        for k in sorted(self.result.keys()):
            for i in range(len(self.functionalityRules[k])):
                r = min(self.fuz.fuzificareTemperatura(temperature,
                                                       self.fuzzyTemperature[self.functionalityRules[k][i][0]],
                                                       self.getColdTuple(), self.getVeryHotTuple(),
                                                       self.getFirstCommon(), self.getLastCommon()),
                        self.fuz.fuzificareCapacitate(capacity,
                                                      self.fuzzyCapacity[self.functionalityRules[k][i][1]]))
                if r != 0 and r not in self.result[k]:
                    self.result[k].append(r)
        x_result = {}
        for k in sorted(self.result.keys()):
            if len(self.result[k]) > 0:
                y = max(self.result[k])
                l = []
                for x in self.drange(0, 20, 1):
                    rs = self.fuz.fuzificarePutere(x, self.fuzzyPower[k])
                    if rs == y:
                        l.append(x)
                x_result[k] = l
        # defuzificare
        numarator = 0
        numitor = 0
        for k in sorted(x_result.keys()):
            for i in x_result[k]:
                numarator += i * max(self.result[k])
            numitor += len(x_result[k]) * max(self.result[k])
        self.defuzi = numarator / numitor
        self.getFirstCommon()
        self.getLastCommon()
        return x_result

    def getDefuzificare(self):
        return self.defuzi

    def getColdTuple(self):
        return self.fuzzyTemperature['cold']

    def getVeryHotTuple(self):
        return self.fuzzyTemperature['veryHot']

    def getFirstCommon(self):
        if self.fuzzyTemperature['cool'][0] in self.fuzzyTemperature['cold']:
            return self.fuzzyTemperature['cool'][0]

    def getLastCommon(self):
        if self.fuzzyTemperature['hot'][len(self.fuzzyTemperature['hot']) - 1] in self.fuzzyTemperature['veryHot']:
            return self.fuzzyTemperature['hot'][len(self.fuzzyTemperature['hot']) - 1]
