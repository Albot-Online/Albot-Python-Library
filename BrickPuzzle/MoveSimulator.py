import BrickPuzzle.BrickPuzzleBoard as Board

def simulateMove(board, move):
    grid = board.getGridClone()
    x, y = getMoveDeltas(board.posX, board.posY, move)

    print(x, y, move)
    if(posOutOfBounds(x, board.size) or posOutOfBounds(y, board.size)):
        return Board.BrickPuzzleBoard(grid=grid, currentPos=[board.posX, board.posY], size=board.size)

    grid[board.posY][board.posX] = grid[y][x]
    grid[y][x] = '0'
    return Board.BrickPuzzleBoard(grid=grid, currentPos=[x, y], size=board.size)




def getMoveDeltas(posX, posY, move):
    if(move == '0'): #Right
        return posX+1, posY
    if(move == '1'): #Up
        return posX, posY-1
    if(move == '2'): #Left
        return posX-1, posY
    return posX, posY+1


def posOutOfBounds(pos, size):
    return pos < 0 and pos > size