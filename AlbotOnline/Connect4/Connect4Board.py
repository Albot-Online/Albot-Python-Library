import AlbotOnline.GridBoard as Grid
from AlbotOnline.Connect4.Connect4Constants import *

class Connect4Board:

    def __init__(self, rawBoard):
        Grid.GridBoard.__init__(self, width=WIDTH, height=HEIGHT, numbers=False, parseString=rawBoard)
        self.rawBoard = rawBoard

    def printBoard(self, title = ""):
        Grid.GridBoard.printBoard(self, title)

    def __str__(self):
        return Grid.GridBoard.__str__(self)