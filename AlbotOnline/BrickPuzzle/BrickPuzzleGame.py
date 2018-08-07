from AlbotOnline import AlbotConnection as AO
import AlbotOnline.BrickPuzzle.MoveSimulator as Simulator
import AlbotOnline.BrickPuzzle.BrickPuzzleBoard as Board

class BrickPuzzleGame:

    def __init__(self, IP = '127.0.0.1', Port = 4000):
        self.connection = AO.AlbotConnection(bufferSize=1024)


    def simulateMove(self, board, move):
        return Simulator.simulateMove(board=board, move=move)

    def getPossibleMoves(self, board):
        moves = []
        if(board.posX < board.size-1): #Right
            moves.append('0')
        if (board.posY > 0):    #Up
            moves.append('1')
        if(board.posX > 0):     #Left
            moves.append('2')
        if (board.posY < board.size-1):  # Down
            moves.append('3')

        return moves

    def makeMoveAndGetNextBoard(self, move):
        self.makeMove(move)
        return self.getNextBoard()

    def getNextBoard(self):
        rawString = self.connection.getNextString()
        return Board.BrickPuzzleBoard(rawString)

    def makeMove(self, move):
        self.connection.sendString(move)

    def makeMoves(self, moves):
        moveString = ""
        for m in moves:
            moveString += m + " "
        self.connection.sendString(moveString)

    def restartGame(self):
        self.connection.sendString("RestartGame")

    def compareBoards(self, b1, b2):
        for y in range(b1.size):
            for x in range(b1.size):
                if(b1.grid[y][x] != b2.grid[y][x]):
                    return False
        return True