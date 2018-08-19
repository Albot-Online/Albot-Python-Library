from AlbotOnline import AlbotConnection as AO
import AlbotOnline.JsonProtocol as Prot
import  AlbotOnline.Connect4.Connect4Board as Board

class Connect4Game:

    def __init__(self, IP='127.0.0.1', Port=4000):
        self.connection = AO.AlbotConnection(bufferSize=1024, IP=IP, Port=Port, gameOverObj=self)
        self.gameOver = False

    def makeMove(self, move):
        self.connection.sendString(str(move))

    def setGameOver(self):
        self.gameOver = True

    def restartGame(self):
        self.connection.restartGame()

    def getNextBoard(self):
        rawBoard = self.connection.getNextJsonField(Prot.FIELDS.board)
        return Board.Connect4Board(rawBoard)

    #TCP-API
    def getPossibleMoves(self, board):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.getPossMoves, Prot.FIELDS.board: board.rawBoard}
        self.connection.sendJsonDict(jCommand)
        return self.connection.getNextJsonField(Prot.FIELDS.possibleMoves)

    def evaluateBoard(self, board):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.evalBoard, Prot.FIELDS.board: board.rawBoard}
        self.connection.sendJsonDict(jCommand)
        return self.connection.getNextJsonField(Prot.FIELDS.boardState)

    def simulateMove(self, board, move, player):
        jCommand = {Prot.FIELDS.action: Prot.ACTIONS.simMove, Prot.FIELDS.board: board.rawBoard}
        jCommand[Prot.FIELDS.move] = move
        jCommand[Prot.FIELDS.player] = player
        self.connection.sendJsonDict(jCommand)
        rawBoard = self.connection.getNextJsonField(Prot.FIELDS.board)
        return Board.Connect4Board(rawBoard)