import sys
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from Controller import Controller
from Sudoku import Sudoku
from State import State

class SudokuGUI(QMainWindow):
    def __init__(self):
        super(SudokuGUI, self).__init__()
        loadUi('SudokuGUI.ui', self)
        self.setWindowTitle("Sudoku")
        self.LoadButton.clicked.connect(self.LoadButtonClicked)
        self.SolveButton.clicked.connect(self.SolveButtonClicked)
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.lightGray)
        self.setPalette(p)

    @pyqtSlot()
    def LoadButtonClicked(self):
        sudoku = Sudoku(State([]), "E:\\Programe\\Python\\Programe\\IA\\Sudoku\\9x9Matrix.txt")
        matrix = sudoku.getInitialSudokuMatrix()
        for i in range(1, len(matrix) + 1):
            for j in range(1, len(matrix) + 1):
                if matrix[i - 1][j - 1] != 0:

                    if i == 1:
                        if j == 1:
                            self.R1C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R1C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R1C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R1C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R1C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R1C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R1C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R1C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R1C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 2:
                        if j == 1:
                            self.R2C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R2C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R2C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R2C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R2C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R2C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R2C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R2C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R2C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 3:
                        if j == 1:
                            self.R3C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R3C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R3C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R3C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R3C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R3C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R3C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R3C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R3C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 4:
                        if j == 1:
                            self.R4C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R4C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R4C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R4C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R4C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R4C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R4C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R4C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R4C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 5:
                        if j == 1:
                            self.R5C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R5C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R5C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R5C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R5C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R5C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R5C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R5C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R5C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 6:
                        if j == 1:
                            self.R6C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R6C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R6C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R6C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R6C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R6C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R6C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R6C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R6C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 7:
                        if j == 1:
                            self.R7C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R7C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R7C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R7C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R7C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R7C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R7C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R7C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R7C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 8:
                        if j == 1:
                            self.R8C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R8C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R8C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R8C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R8C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R8C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R8C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R8C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R8C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 9:
                        if j == 1:
                            self.R9C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R9C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R9C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R9C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R9C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R9C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R9C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R9C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R9C9.setText(" " + str(matrix[i - 1][j - 1]))

    @pyqtSlot()
    def SolveButtonClicked(self):
        sudoku = Sudoku(State([]), "E:\\Programe\\Python\\Programe\\IA\\Sudoku\\9x9Matrix.txt")
        controller = Controller(sudoku)
        result = controller.BFS(controller.getSudoku())
        if result[0] == None:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("No solution found !")
            msg.setWindowTitle("Resolving error")
            msg.exec_();
        else:
            matrix = result[0].getMatrix()
            for i in range(1, len(matrix) + 1):
                for j in range(1, len(matrix) + 1):
                    if i == 1:
                        if j == 1:
                            self.R1C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R1C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R1C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R1C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R1C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R1C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R1C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R1C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R1C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 2:
                        if j == 1:
                            self.R2C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R2C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R2C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R2C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R2C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R2C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R2C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R2C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R2C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 3:
                        if j == 1:
                            self.R3C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R3C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R3C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R3C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R3C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R3C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R3C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R3C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R3C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 4:
                        if j == 1:
                            self.R4C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R4C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R4C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R4C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R4C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R4C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R4C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R4C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R4C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 5:
                        if j == 1:
                            self.R5C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R5C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R5C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R5C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R5C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R5C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R5C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R5C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R5C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 6:
                        if j == 1:
                            self.R6C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R6C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R6C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R6C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R6C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R6C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R6C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R6C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R6C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 7:
                        if j == 1:
                            self.R7C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R7C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R7C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R7C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R7C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R7C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R7C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R7C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R7C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 8:
                        if j == 1:
                            self.R8C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R8C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R8C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R8C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R8C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R8C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R8C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R8C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R8C9.setText(" " + str(matrix[i - 1][j - 1]))
                    elif i == 9:
                        if j == 1:
                            self.R9C1.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 2:
                            self.R9C2.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 3:
                            self.R9C3.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 4:
                            self.R9C4.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 5:
                            self.R9C5.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 6:
                            self.R9C6.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 7:
                            self.R9C7.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 8:
                            self.R9C8.setText(" " + str(matrix[i - 1][j - 1]))
                        elif j == 9:
                            self.R9C9.setText(" " + str(matrix[i - 1][j - 1]))



app = QApplication(sys.argv)
widget = SudokuGUI()
widget.show()
sys.exit(app.exec_())