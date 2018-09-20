from AlbotOnline.Connect4 import Connect4Game

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
    while(True):
        game.makeMove(int(input()))
        board = game.getNextBoard()
        board.printBoard("My current board")

#testConnect4()

