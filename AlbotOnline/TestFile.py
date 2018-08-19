from AlbotOnline.Connect4 import Connect4Game
from AlbotOnline.Snake import SnakeGame
import AlbotOnline.JsonProtocol as Prot
import random as rand


'''
game = Connect4Game.Connect4Game()
board = game.getNextBoard()
print(board.width)
print(board.height)
print(board.grid)
board.printBoard("My current board")

moves = game.getPossibleMoves(board)
print(moves)

state = game.evaluateBoard(board)
print(state)

print(board.rawBoard)
simBoard = game.simulateMove(board, 3, '1')
simBoard.printBoard()

input("restart...")
game.restartGame()
input("ok?")
'''
game = SnakeGame.SnakeGame() #Connects you to the Client
maxDepth = 3

def stateToScore(state):
    if(state == Prot.STATES.ongoing):
        return 0.5
    if(state == Prot.STATES.draw):
        return 0.25
    if (state == Prot.STATES.playerWon):
        return 1
    if (state == Prot.STATES.enemyWon):
        return 0

def search(board, depth):
    state = game.evaluateBoard(board)
    if(depth == 0 or state != Prot.STATES.ongoing):
        return stateToScore(state), "None"

    pMoves, eMoves = game.getPossibleMoves(board)

    results = {}
    for p in pMoves:
        results[p] = 0
        for e in eMoves:
            simBoard = game.simulateMove(board, p, e)
            score, ignore = search(simBoard, depth-1)
            results[p] += score / len(eMoves)

    maxScore = results[pMoves[0]]
    move = pMoves[0]
    for i in range(1,3):
        if results[pMoves[i]] >= maxScore:
            maxScore = results[pMoves[i]]
            move = pMoves[i]

    if(depth == maxDepth):
        print("******************s")
        temp = [[p, results[p]] for p in pMoves]
        temp.sort(key=lambda  r: r[1], reverse=True)
        print("Sorted", temp)
        temp = [p for p in temp if p[1] >= temp[0][1]]
        pick = rand.choice(temp)
        return pick[1], pick[0]

    return maxScore, move

while True:
    while(game.gameOver == False):
        board = game.getNextBoard()
        if(game.gameOver):
            break

        score, move = search(board, maxDepth)
        if(len(board.blocked) > 0):
            print(board.blocked[0])
        print(score, move)
        board.printBoard("My current board")

        game.makeMove(move)

    game.restartGame()