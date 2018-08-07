import socket
import json

class AlbotConnection:

    def __init__(self, bufferSize = 1024, IP = '127.0.0.1', Port = 4000):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bufferSize = bufferSize

        self.connection.connect((IP, Port))
        print("Connected to Albot, waiting for game to start...")


    def sendString(self, data):
        self.connection.send(bytes(data, "utf-8"))

    def getNextString(self):
        data = self.connection.recv(self.bufferSize)
        return data.decode("utf-8")

    def getNextJsonMsg(self):
        return json.dumps(self.getNextString())
