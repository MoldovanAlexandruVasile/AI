from Controller import Controller
from Sudoku import Sudoku
from State import State


class UI:
    def __init__(self):
        self.runSudoku()

    def printMainMenu(self):
        print("\n\tMethod:")
        print("\t\t1. BFS.")
        print("\t\t2. GBFS.")
        print("\t\t0. Back.")

    def printSudokuChose(self):
        print("Sudoku table:")
        print("1. 9x9")
        print("2. 4x4")
        print("0. Exit")

    def mainMenu(self, controller):
        while True:
            self.printMainMenu()
            command = int(input("\t\t\t Your command: "))
            if command == 1:
                result = controller.BFS(controller.getSudoku())
                print(result[0])
                print("Total steps done: " + str(result[1]))
            elif command == 2:
                result = controller.GBFS(controller.getSudoku())
                print(result[0])
                print("Total steps done: " + str(result[1]))
            else:
                break

    def runSudoku(self):
        while True:
            self.printSudokuChose()
            command = int(input("\t Your command: "))
            if command == 1:
                sudoku = Sudoku(State([]), "E:\\Programe\\Python\\Programe\\IA\\Sudoku\\9x9Matrix.txt")
                controller = Controller(sudoku)
                self.mainMenu(controller)
            elif command == 2:
                sudoku = Sudoku(State([]), "E:\\Programe\\Python\\Programe\\IA\\Sudoku\\4x4Matrix.txt")
                controller = Controller(sudoku)
                self.mainMenu(controller)
            else:
                break
