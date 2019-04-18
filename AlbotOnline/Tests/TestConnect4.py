from AlbotOnline.Connect4 import Connect4Game
import AlbotOnline.JsonProtocol as Prot


def testConnect4():
    game = Connect4Game.Connect4Game()
    board = game.getNextBoard()
    board.printBoard("My current board")

    moves = game.getPossibleMoves(board)
    print(moves)

    state = game.evaluateBoard(board)
    print(state)

    simBoard = game.simulateMove(board, 3, 1)
    simBoard.printBoard("Siiim board")

    simBoard = game.simulateMove(simBoard, 3, 1)
    simBoard.printBoard("Siiim board")
    while (True):
        game.makeMove(int(input()))
        board = game.getNextBoard()
        board.printBoard("My current board")


def testGameLoop(game, decideMoveFunc, autoRestart=False):
    while (True):
        if (game.awaitNextGameState() != Prot.STATES.ongoing):
            if (autoRestart):
                game.restartGame()
                continue
            else:
                break

        move = decideMoveFunc(game.currentBoard)
        game.makeMove(move)


def decideMove(board):
    moves = game.getPossibleMoves(board)
    return moves[0]


# game = None
if (__name__ == "__main__"):
    game = Connect4Game.Connect4Game()
    # testGameLoop(game, decideMove, False)
    game.playGame(decideMove, True)
