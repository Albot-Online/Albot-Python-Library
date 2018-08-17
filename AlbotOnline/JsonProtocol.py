#Fields
STATES = lambda: None
STATES.ongoing = "ongoing"
STATES.playerWon = "playerWon"
STATES.enemyWon = "enemyWon"
STATES.draw = "draw"

#Fields
FIELDS = lambda: None
FIELDS.board = "board"
FIELDS.evaluate = "evaluate"
FIELDS.possibleMoves = "possMoves"
FIELDS.winner = "winner"
FIELDS.move = "move"
FIELDS.player = "player"
FIELDS.enemy = "enemy"
FIELDS.action = "action"
FIELDS.boardState = "boardState"
FIELDS.gameOver = "gameOver"

#Fields Snake
FIELDS.Snake = lambda: None
FIELDS.Snake.direction = "dir"
FIELDS.Snake.posX = "x"
FIELDS.Snake.posY = "y"
FIELDS.Snake.blocked = "blocked"
FIELDS.Snake.playerMove = "playerMove"
FIELDS.Snake.enemyMove = "enemyMove"
FIELDS.Snake.playerMoves = "playerMoves"
FIELDS.Snake.enemyMoves = "enemyMoves"
FIELDS.Snake.enemyMoves = "enemyMoves"

#Actions
ACTIONS = lambda: None
ACTIONS.makeMove = "makeMove"
ACTIONS.simMove = "simulateMove"
ACTIONS.evalBoard = "evaluateBoard"
ACTIONS.getPossMoves = "getPossibleMoves"
ACTIONS.restart = "RestartGame"

#Actions Snake
ACTIONS.Snake = lambda: None
ACTIONS.Snake.up = "up"
ACTIONS.Snake.down = "down"
ACTIONS.Snake.left = "left"
ACTIONS.Snake.right = "right"
ACTIONS.Snake.simMoveDelta = "simulateMoveDelta"