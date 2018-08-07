import JsonProtocol as Prot
import math

class BrickPuzzleBoard:

    #Currently does not use Json formatting
    def __init__(self, rawJson = None, grid = None, currentPos = None, size = None):
        self.hasCheckedForVictory = False

        if(grid == None):
            self._parseBoard(rawJson)
        else:
            self.grid = grid
            self.size = size
            self.posX = currentPos[0]
            self.posY = currentPos[1]


    def _parseBoard(self, rawBoard):
        cells = rawBoard.split(' ')
        self.size = int( round(math.sqrt(len(cells))) )
        self.grid = []

        for y in range(self.size):
            row = []
            for x in range(self.size):
                cell = cells[self.size*y + x]
                row.append(cell)
                if(cell == '0'):
                    self.posX = x
                    self.posY = y
            self.grid.append(row)

    def getGridClone(self):
        newGrid = []
        for row in self.grid:
            newGrid.append(row.copy())
        return newGrid

    # ********* Victory Checks
    def isBoardFinished(self):
        return self.victory if self.hasCheckedForVictory else self.checkForVictory()

    def checkForVictory(self):
        self.hasCheckedForVictory = True
        self.victory = True
        for y in range(self.size):
            for x in range(self.size):
                if(x + y*self.size != int(self.grid[y][x])):
                    self.victory = False
                    return False
        return True

    #********* Debugging
    def printBoard(self):
        print("************")
        print(self)
        print("************")
    def __str__(self):
        temp = ""
        for s in self.grid:
            temp += str(s) + "\n"
        return  temp