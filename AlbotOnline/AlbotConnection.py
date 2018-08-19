import socket
import json
import AlbotOnline.JsonProtocol as Protocol

class AlbotConnection:

    def __init__(self, bufferSize = 1024, IP = '127.0.0.1', Port = 4000, gameOverObj = None):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bufferSize = bufferSize
        self.awaitingData = True
        self.connection.connect((IP, Port))
        self.gameOverObj = gameOverObj
        print("Connected to Albot, waiting for game to start...")


    #Communication Output
    def sendString(self, data):
        self.awaitingData = True
        self.connection.send(bytes(data, "utf-8"))

    def sendJsonDict(self, data):
        self.sendString(json.dumps(data))

    def sendAction(self, data, action):
        data[Protocol.FIELDS.action] = action
        self.sendJsonDict(data)

    #Communication Input
    def getNextString(self, checkForGameOver = False):
        data = self.connection.recv(self.bufferSize)
        text = data.decode("utf-8")
       # print(text)
        self.awaitingData = False

        if(checkForGameOver and Protocol.FIELDS.gameOver in text):
            if(self.gameOverObj != None):
                self.gameOverObj.setGameOver(text)

        return text

    def getNextJsonMsg(self, checkForGameOver = False):
        return json.loads(self.getNextString(checkForGameOver))

    def getNextJsonField(self, field):
        return self.getNextJsonMsg()[field]




    #Actions
    def restartGame(self):
        self.sendString(Protocol.ACTIONS.restart)

