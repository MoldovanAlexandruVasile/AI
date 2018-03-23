from copy import deepcopy
from State import State


class Sudoku:
    def __init__(self, initialSudoku, fileName):
        self.__initialSudoku = initialSudoku
        self.readSudokuFromFile(fileName)

    def readSudokuFromFile(self, fileName):
        file = open(fileName)
        table = []
        try:
            n = int(file.readline())
            for i in range(n):
                aux = []
                line = file.readline()
                line = line.split(" ")
                for v in line:
                    aux.append(int(v))
                table.append(aux)
            self.__initialSudoku.setMatrix(table)
        except Exception as error:
            print("Can not read from the file !")

    def euristic(self, state1, state2):
        coordinates = state1.findEmptyLocation()
        i = coordinates[0]
        j = coordinates[1]
        freq = state1.getFrequencies()
        value = state2.getValueFrom(i, j)
        return freq[value - 1][1]

    def expand(self, state):
        result = []
        coordinates = state.findEmptyLocation()
        i = coordinates[0]
        j = coordinates[1]
        rowValues = state.getAvailableValuesForRow(i)
        colValues = state.getAvailableValuesForColumn(j)
        boxValues = state.getAvailableValuesForBox(i, j)
        for rowValue in rowValues:
            if rowValue in colValues and rowValue in boxValues:
                newSudoku = State(deepcopy(state.getMatrix()))
                newSudoku.setValueTo(i, j, rowValue)
                result.append(newSudoku)
        return result

    def isCompleted(self, state):
        coordinates = state.findEmptyLocation()
        i = coordinates[0]
        j = coordinates[1]
        if i >= 0 and j >= 0:
            return False
        return True

    def getInitialSudoku(self):
        return self.__initialSudoku

    def getInitialSudokuMatrix(self):
        return self.__initialSudoku.getMatrix()

    def setInitialSudoku(self, initial):
        self.__initialSudoku = initial

    def getSize(self):
        return self.__initialSudoku.getSize()
