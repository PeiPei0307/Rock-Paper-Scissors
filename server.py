from ast import Pass
import asyncio, random, socket, json, time, threading

Randomlist = ["Rock", "Paper", "Scissors"]
Room = [{"Type":"Result", "Player":None, "Push":None, "Gamestage":None, "transport":None},
        {"Type":"Result", "Player":None, "Push":None, "Gamestage":None, "transport":None}]

class GameServer(asyncio.Protocol):
    def __init__(self):
        self.callback = {"Stage":"None", "P2Stage": "None"}

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''

        if Room[0]["Player"] and Room[1]["Player"] != None:
            self.transport.write(b'{"Stage":Roomfull}')
        if Room[0]["Player"] == None:
            Room[0]["Player"], Room[0]["transport"] = self.address, self.transport
        else:
            Room[1]["Player"], Room[1]["transport"] = self.address, self.transport

        print('Accepted connection from {}'.format(self.address))

    def data_received(self, data):

        data = data.decode("utf-8")
        data = json.loads(data)

        print(data, self.address)
        print(self.callback, self.address)

        if Room[0]["Player"] or Room[1]["Player"] == None:
            self.callback["P2Stage"] = None

        if data["GameStage"] == "WaitP2":
            for i in Room:
                if i["Player"] != self.address and i["Gamestage"] != None:
                    self.callback["P2Stage"] = "P2WaitPunch"
            if Room[0]["Player"] and Room[1]["Player"] != None:
                self.callback["Stage"] = "P2Join"
                self.transport.write(json.dumps(self.callback).encode("utf-8"))
            else:
                self.callback["Stage"] = "WaitP2"
                self.transport.write(json.dumps(self.callback).encode("utf-8"))

        if data["GameStage"] == "WaitPunch":
            for i in Room:
                if i["Player"] != self.address and i["Gamestage"] == None:
                    self.callback["P2Stage"] = "WatingP2"
            self.callback["Stage"] = "WaitPunch"
            self.transport.write(json.dumps(self.callback).encode("utf-8"))
            
        if data["GameStage"] == "Rock" or "Paper" or "Scissors":
            self.transport.write(json.dumps(self.callback).encode("utf-8"))
            for i in Room:
                if i["Player"] == self.address:
                    i["Push"] = data["GameStage"]

                   

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))

            if Room[0]["Player"] == self.address :
                for key in Room[0]:
                    Room[0][key] = None
                Room[1]["Gamestage"] = None
            else:
                for key in Room[1]:
                    Room[1][key] = None
                    Room[0]["Gamestage"] = None

        elif self.data:
            print('Client {} sent {} but then closed'
                  .format(self.address, self.data))
        else:
            print('Client {} closed socket'.format(self.address))

def RunServer():
    address = ("127.0.0.1", 1060)
    loop = asyncio.get_event_loop()
    coro = loop.create_server(GameServer, *address)
    server = loop.run_until_complete(coro)
    print('Listening at {}'.format(address))
    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()

def GetPort():  
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port

def Channel():
    while True:
        if Room[0]["Player"] or Room[1]["Player"] != None:
            if Room[0]["Player"] == None:
                Room[1]["transport"]
                


if __name__ == '__main__':
    Channel = threading.Thread(target = Channel)
    Channel.start()

    RunServer()
