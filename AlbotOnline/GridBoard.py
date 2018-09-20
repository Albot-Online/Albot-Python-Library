import copy

class GridBoard:

    def __init__(self, width, height, numbers = True, parseString = ""):
        self.width = width
        self.height = height
        if(parseString == ""):
            self.createEmptyGrid(numbers)
        else:
            GridBoard.parseBoard(self, parseString)

    def createEmptyGrid(self, numbers):
        self.grid = []
        emptySign = 0 if numbers else '0'
        for y in range(self.height):
            self.grid.append([emptySign for x in range(self.width)])


    def parseBoard(self, parseString):
        words = parseString.split(' ')
        self.grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(words[y*self.width + x])
            self.grid.append(row)


    def cloneGrid(self):
        return copy.deepcopy(self.grid)

    def printBoard(self, title =""):
        print("* * * * *{0}* * * * * *".format(title))
        print(self)
        print("* * * * * * * * * * *")

    def __str__(self):
        rows = [" ".join(self.grid[y]) + '\n' for y in range(self.height)]
        return "".join(rows)
