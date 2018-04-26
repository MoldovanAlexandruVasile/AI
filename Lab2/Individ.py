from random import *


class Individ:
    def __init__(self, cubes, exactCopy=False):
        if exactCopy:
            # makes an exact copy of the Individ
            self.cubes = cubes[:]
        else:
            # Shuffles all the cubes from the Individ
            self.cubes = [Individ.rotateCube(i, 6)[:] for i in cubes]

    def fitness(self):
        # return the side faces
        cubes2 = sorted([Individ.remove(i) for i in self.cubes])
        maxLen = 0
        currentElem = None
        currentSeqLen = 0
        for elem in cubes2:
            # taking first cube from cubes
            if currentElem is None:
                currentSeqLen += 1
                currentElem = elem
            # verify if the sequence continues
            elif currentElem == elem:
                currentSeqLen += 1
            # start a new sequence
            else:
                maxLen = max(currentSeqLen, maxLen)
                currentSeqLen = 1
                currentElem = elem
        maxLen = max(currentSeqLen, maxLen)
        return maxLen

    # Mutates a random cube
    def mutate(self, prob):
        if prob > random():
            pos = int(random() * len(self.cubes))
            self.cubes[pos] = self.rotateCube(self.cubes[pos], 6)

    def __str__(self):
        return str(self.cubes)

    @staticmethod
    def remove(elem):
        return elem[:2] + elem[3:5]

    @staticmethod
    def rotateCube(cube, noOfRotations):
        for _ in range(0, noOfRotations):
            pos = randint(1, 3)
            if pos == 1:
                cube[1], cube[2], cube[4], cube[5] = cube[2], cube[4], cube[5], cube[1]
            elif pos == 2:
                cube[0], cube[5], cube[3], cube[2] = cube[5], cube[3], cube[2], cube[0]
            elif pos == 3:
                cube[3], cube[4], cube[0], cube[1] = cube[4], cube[0], cube[1], cube[3]
        return cube

    @staticmethod
    def crossOver(ind1, ind2):
        # Take a random position in Individ.cubes and concatenate first part from ind1 with the second part from ind2 from the cut pos
        cutOver = int(random() * len(ind1.cubes))
        newIndivid = []
        for i in range(0, cutOver):
            newIndivid.append(ind1.cubes[i][:])
        for i in range(cutOver, len(ind2.cubes)):
            newIndivid.append(ind2.cubes[i][:])
        return Individ(newIndivid, True)
