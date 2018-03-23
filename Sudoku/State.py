from math import sqrt


class State:
    def __init__(self, matrix):
        self.__matrix = matrix
        self.__size = len(matrix)

    def usedInRow(self, row):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__matrix[row][i] == self.__matrix[row][j]:
                    return True
        return False

    def usedInCol(self, col):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__matrix[i][col] == self.__matrix[j][col]:
                    return True
        return False

    def usedInBox(self, row, col):
        for i in range(int(sqrt(self.__size))):
            for j in range(int(sqrt(self.__size))):
                if self.__matrix[i + row][j + col] == self.__matrix[j + row][i + col]:
                    return True
        return False

    def getAvailableValuesForRow(self, i):
        numbers = range(1, self.__size + 1)
        fromRow = []
        for j in range(self.__size):
            fromRow.append(self.__matrix[i][j])
        return [number for number in numbers if number not in fromRow]

    def getAvailableValuesForColumn(self, j):
        numbers = range(1, self.__size + 1)
        fromColumn = []
        for i in range(self.__size):
            fromColumn.append(self.__matrix[i][j])
        return [number for number in numbers if number not in fromColumn]

    def getAvailableValuesForBox(self, i, j):
        row = 0
        column = 0
        cadrani = i // int(sqrt(self.__size))
        cadranj = j // int(sqrt(self.__size))

        if cadrani == 0 and cadranj == 0:
            row = 0
            column = 0
        elif cadrani == 0 and cadranj == 1:
            row = 0
            column = int(sqrt(self.__size))
        elif cadrani == 0 and cadranj == 2:
            row = 0
            column = 2 * int(sqrt(self.__size))
        elif cadrani == 1 and cadranj == 0:
            row = int(sqrt(self.__size))
            column = 0
        elif cadrani == 1 and cadranj == 1:
            row = int(sqrt(self.__size))
            column = int(sqrt(self.__size))
        elif cadrani == 1 and cadranj == 2:
            row = int(sqrt(self.__size))
            column = 2 * int(sqrt(self.__size))
        elif cadrani == 2 and cadranj == 0:
            row = 2 * int(sqrt(self.__size))
            column = 0
        elif cadrani == 2 and cadranj == 1:
            row = 2 * int(sqrt(self.__size))
            column = int(sqrt(self.__size))
        elif cadrani == 2 and cadranj == 2:
            row = 2 * int(sqrt(self.__size))
            column = 2 * int(sqrt(self.__size))

        numbers = range(1, self.__size + 1)
        fromBox = []
        for r in range(row, row + int(sqrt(self.__size)) - 1):
            for c in range(column, column + int(sqrt(self.__size)) - 1):
                fromBox.append(self.__matrix[r][c])
        return [number for number in numbers if number not in fromBox]

    def getFrequencies(self):
        freq = []
        for i in range(1, self.__size + 1):
            freq.append([i, 0])
        for row in self.__matrix:
            for elem in row:
                if elem != 0:
                    freq[elem - 1][1] += 1
        return freq

    def findEmptyLocation(self):
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__matrix[i][j] == 0:
                    return [i, j]
        return [-1, -1]

    def setValueTo(self, i, j, value):
        self.__matrix[i][j] = value

    def getValueFrom(self, i, j):
        return self.__matrix[i][j]

    def getSize(self):
        return self.__size

    def getMatrix(self):
        return self.__matrix

    def setMatrix(self, matrix):
        self.__matrix = matrix
        self.__size = len(matrix[0])

    def __str__(self):
        result = ""
        for line in self.__matrix:
            for number in line:
                result = result + " " + str(number)
            result = result + "\n"
        return result
