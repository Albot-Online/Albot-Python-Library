from AlbotOnline.Snake import SnakeGame
import AlbotOnline.JsonProtocol as Prot
import numpy as np


def decideMove(board):
    moves = game.getPossibleMoves(board)[0]
    print(moves)
    return moves[np.random.choice(len(moves))]


if (__name__ == "__main__"):
    game = SnakeGame.SnakeGame()
    game.playGame(decideMove, True)
