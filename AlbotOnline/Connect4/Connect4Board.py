import AlbotOnline.GridBoard as Grid
from AlbotOnline.Connect4.Connect4Constants import *


class Connect4Board:

    def __init__(self, grid):
        self.grid = grid

    def printBoard(self, title=""):
        Grid.GridBoard.printBoard(self, title)

    def __str__(self):
        temp = ""
        for row in self.grid:
            for cell in row:
                temp += str(cell) + "\t"
            temp += "\n"
        return temp
