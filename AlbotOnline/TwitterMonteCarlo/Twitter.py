from AlbotOnline import AlbotConnection as AO

class TwitterSampler:

    def __init__(self, IP = '127.0.0.1', Port = 4000):
        self.connection = AO.AlbotConnection(bufferSize=1024, IP=IP, Port=Port, gameOverObj=self)
        self.width = 2048
        self.height = 2048

    def getSample(self, x, y):
        self.connection.sendString(str(x) + " " + str(y))
        response = self.connection.getNextString()

        if(response == "HIT"):
            return True
        elif(response == "MISS"):
            return False

        return response