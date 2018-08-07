import BrickPuzzle.BrickPuzzleGame as AO
import BrickPuzzle.BrickPuzzleBoard as B

game = AO.BrickPuzzleGame()
b = game.getNextBoard()

b.printBoard()
print(game.getPossibleMoves(b))
move = input("Move: ")

simBoard = game.simulateMove(b, move)

simBoard.printBoard()
print(simBoard.isBoardFinished())

game.makeMove(move)