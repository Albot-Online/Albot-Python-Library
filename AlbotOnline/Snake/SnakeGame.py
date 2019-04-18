from AlbotOnline import AlbotConnection as AO
from AlbotOnline.Snake.SnakeBoard import SnakeBoard
import AlbotOnline.JsonProtocol as Prot
import json


class SnakeGame:

    def __init__(self, IP='127.0.0.1', Port=4000):
        self.connection = AO.AlbotConnection(bufferSize=16384, IP=IP, Port=Port, gameOverObj=self)
        self._initGameVars()

    def _initGameVars(self):
        self.currentBoard = SnakeBoard()
        self.gameOver = False

    def getNextBoard(self, oldBoard=None):
        if (self.connection.awaitingData == False):
            self.makePassMove()

        jMsg = self.connection.getNextJsonMsg()
        if (oldBoard != None):
            return SnakeBoard(oldBoard=oldBoard, jUpdate=jMsg)
        else:
            return SnakeBoard(jUpdate=jMsg)

    def awaitNextGameState(self):
        jMsg = self.connection.getNextJsonMsg()
        self.currentBoard = SnakeBoard(jUpdate=jMsg)
        self.boardState = jMsg[Prot.FIELDS.boardState]
        self.gameOver = self.boardState != Prot.STATES.ongoing

        return self.boardState

    def restartGame(self):
        self.connection.restartGame()
        self._initGameVars()

    def setGameOver(self, msg):
        self.gameOver = True
        self.currentBoard.gameOver = True
        print(msg)

    # makeMoves
    def makePassMove(self):
        self.connection.sendString(" ")

    def moveUp(self):
        self.connection.sendString(Prot.ACTIONS.Snake.up)

    def moveDown(self):
        self.connection.sendString(Prot.ACTIONS.Snake.down)

    def moveLeft(self):
        self.connection.sendString(Prot.ACTIONS.Snake.left)

    def moveRight(self):
        self.connection.sendString(Prot.ACTIONS.Snake.right)

    def makeMove(self, dir):
        if (dir == Prot.ACTIONS.Snake.up):
            self.moveUp()
        elif (dir == Prot.ACTIONS.Snake.down):
            self.moveDown()
        elif (dir == Prot.ACTIONS.Snake.left):
            self.moveLeft()
        elif (dir == Prot.ACTIONS.Snake.right):
            self.moveRight()

    def makeMoveInt(self, dir):
        self.makeMove(self.intToMove(dir))

    def intToMove(self, dir):
        if (dir == 0):
            return Prot.ACTIONS.Snake.right
        elif (dir == 1):
            return Prot.ACTIONS.Snake.up
        elif (dir == 2):
            return Prot.ACTIONS.Snake.left
        elif (dir == 3):
            return Prot.ACTIONS.Snake.down

    # Raw msg handling
    def getnextJsonMsg(self):
        return self.connection.getNextJsonMsg()

    def getNextTCPStringMsg(self):
        return self.connection.getNextString()

    # TCP API
    def simulateMove(self, board, playerMove, enemyMove):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.Snake.simMoveDelta, Prot.FIELDS.player: board.raw2Player,
                    Prot.FIELDS.enemy: board.rawEnemy}
        jCommand[Prot.FIELDS.Snake.playerMove] = playerMove
        jCommand[Prot.FIELDS.Snake.enemyMove] = enemyMove
        self.connection.sendJsonDict(jCommand)
        return self.getNextBoard(oldBoard=board)

    def evaluateBoard(self, board):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.evalBoard, Prot.FIELDS.board: board.getAPIBoard()}
        self.connection.sendJsonDict(jCommand)
        return self.connection.getNextJsonField(Prot.FIELDS.boardState)

    def getPossibleMoves(self, board):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.getPossMoves, Prot.FIELDS.player: board.player.dir,
                    Prot.FIELDS.enemy: board.enemy.dir}
        self.connection.sendJsonDict(jCommand)
        jResponse = self.connection.getNextJsonMsg()
        return jResponse[Prot.FIELDS.Snake.playerMoves], jResponse[Prot.FIELDS.Snake.enemyMoves]

    def playGame(self, decideMoveFunc, autoRestart=False):
        while (True):
            if (self.awaitNextGameState() != Prot.STATES.ongoing):
                if (autoRestart):
                    self.restartGame()
                    continue
                else:
                    break

            move = decideMoveFunc(self.currentBoard)
            self.makeMove(move)
