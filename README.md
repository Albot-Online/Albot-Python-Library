# Albot.Online Python Library

A simple library for communicating with the [Albot.Online](https://Albot.Online) client. 
This is great for getting you up and running fast, allowing you to focus more on your AI logic.
<br><br>
## Getting Started
This library is available at [PyPi](https://Pypi.org), so to download and install simply use the command:<br>
```
pip install Albot.Online
```
## Example
Following is a short example of the Python Library being put to use on the [Snake](https://www.albot.online/snake/) game. 
For exact information of how to use the library see the [documentation Wiki](https://github.com/Albot-Online/Albot-Python-Library/wiki).

```python
from AlbotOnline.Snake.SnakeGame import SnakeGame
import random

game = SnakeGame() #Connects you to the Client
while(game.gameOver == False):
    board = game.getNextBoard()
    board.printBoard("Current Board")

    playerMoves, enemyMoves = game.getPossibleMoves(board)
    game.makeMove(random.choice(playerMoves))
```
This bot will simply connect to the client, look at what moves it currently has available and pick one at random.
<br><br>


## Versioning

  0.2b0
  
## Authors

  Fredrik Carlsson

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Albot-Online/Albot-Python-Library/blob/master/LICENSE) file for details
