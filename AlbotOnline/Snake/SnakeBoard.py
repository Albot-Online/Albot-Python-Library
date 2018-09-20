import AlbotOnline.GridBoard as Grid
from AlbotOnline.Snake.SnakeConstants import Constants as C
import AlbotOnline.JsonProtocol as Prot
import copy

class SnakeBoard(Grid.GridBoard):

    def __init__(self, oldBoard = None, jUpdate = None):
        self.blocked = []
        if(oldBoard == None):
            Grid.GridBoard.__init__(self, width=C.width, height=C.height, numbers=False)
        elif(oldBoard != None):
            self._copyOldBoard(oldBoard)

        if(jUpdate != None):
            self._parseJsonMsg(jUpdate)

    def _parseJsonMsg(self, jUpdate):
        self.blocked.extend(jUpdate[Prot.FIELDS.Snake.blocked])
        self._parseBlocked(jUpdate[Prot.FIELDS.Snake.blocked])

        self.rawPlayer = jUpdate[Prot.FIELDS.player]
        self.raw2Player = {}
        self.raw2Player['x'] = self.rawPlayer['x']
        self.raw2Player['y'] = self.rawPlayer['y']
        self.player = self._parseSnakePlayer(self.rawPlayer, C.playerSign)

        self.rawEnemy = jUpdate[Prot.FIELDS.enemy]
        self.enemy = self._parseSnakePlayer(self.rawEnemy, C.enemySign)

    def _parseSnakePlayer(self, snakePlayerField, gridSign):
        temp = lambda: None
        temp.dir = snakePlayerField[Prot.FIELDS.Snake.direction]
        temp.x = snakePlayerField[Prot.FIELDS.Snake.posX]
        temp.y = snakePlayerField[Prot.FIELDS.Snake.posY]
        if(temp.x < C.width and temp.x >= 0 and temp.y < C.height and temp.y >= 0):
            self.grid[temp.y][temp.x] = gridSign
        return temp

    def _parseBlocked(self, blocked):
        for b in blocked:
            self.grid[b[Prot.FIELDS.Snake.posY]][b[Prot.FIELDS.Snake.posX]] = C.blockedSign

    def _copyOldBoard(self, oldBoard):
        self.grid = oldBoard.cloneGrid()
        self.height = oldBoard.height
        self.width = oldBoard.width
        self.blocked = copy.deepcopy(oldBoard.blocked)

    def printBoard(self, title=""):
        Grid.GridBoard.printBoard(self, title)

    #TCP API
    def getAPIBoard(self):
        return {Prot.FIELDS.player: self.rawPlayer, Prot.FIELDS.enemy: self.rawEnemy, Prot.FIELDS.Snake.blocked: self.blocked}

    def getAPIPlayers(self):
        return {Prot.FIELDS.player: self.rawPlayer, Prot.FIELDS.enemy: self.rawEnemy}