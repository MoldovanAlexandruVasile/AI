class Controller:
    def __init__(self, sudoku):
        self.__sudoku = sudoku

    def BFS(self, sudoku):
        queue, visited = [], []
        step = 0
        queue.append(sudoku.getInitialSudoku())
        while queue:
            state = queue.pop()
            step = step + 1
            if sudoku.isCompleted(state):
                return [state, step]
            elif state not in visited:
                visited.append(state)
                queue += sudoku.expand(state)
        return None, step

    def GBFS(self, sudoku):
        queue, visited = [], []
        step = 0
        queue.append(sudoku.getInitialSudoku())
        while queue:
            state = queue.pop()
            step = step + 1
            if sudoku.isCompleted(state):
                return [state, step]
            elif state not in visited:
                visited.append(state)
                queue += sorted(sudoku.expand(state), key=lambda iteratedState: sudoku.euristic(state, iteratedState))
        return None, step

    def getSudoku(self):
        return self.__sudoku

    def setSudoku(self, sudoku):
        self.__sudoku = sudoku
