from ast import Pass
import asyncio, random, socket, json, time, threading

Clientlist = []
Stagelist = ["Rock", "Paper", "Scissors"]
Room = {"Stage":"Result",
        "player1":None, "player2":None,
        "P1Stage":None, "P2Stage":None }

class GameServer(asyncio.Protocol):
    def __init__(self):
        self.Player = {"address":None, "transport":None}
        self.callback = {}

    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        
        self.Player["address"] = self.address
        self.Player["transport"] = self.transport
        Clientlist.append(self.Player)

        if Room["player1"] and Room["player2"] != None:
            self.transport.write(b'{"Stage":Roomfull}')
        if Room["player1"] == None:
            Room["player1"] = self.address
        else:
            Room["player2"] = self.address

        print('Accepted connection from {}'.format(self.address))

        """
        for i in range(2):
            if Room['player' + str(i + 1)] == None:
                Room['player' + str(i + 1)] = self.address
                break
            else:
                self.transport.write(b'{"Stage":Roomfull}')
        """

    def data_received(self, data):

        data = data.decode("utf-8")
        data = json.loads(data)

        if data["Role"] == "Client":
            if data["State"] == "Waitingpunch":
                self.callback["Stage"] = random.choice(Stagelist)
                self.transport.write(json.dumps(self.callback).encode("utf-8"))
            if data["State"] != "Waitingpunch":
                if Room["player1"] == self.address:
                    Room["P1Stage"] = data["State"]
                if Room["player2"] == self.address:
                    Room["P2Stage"] = data["State"]       

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))

            Clientlist.remove({"transport":self.transport, "address":self.address})
            if Room["player1"] == self.address :
                Room["player1"] = None
            else:
                Room["player2"] = None

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
        time.sleep(1)
        if Room["P1Stage"] != None and Room["P2Stage"] != None:
            print("Channel")
            for client in Clientlist:
                client["transport"].write(json.dumps(Room).encode("utf-8"))
            Room["P1Stage"] = None
            Room["P2Stage"] = None

        """
        if Clientlist:
            for client in Clientlist:
                print("In channel : ", client["address"])
                client["transport"].write(b'{"Datatype":"Channel", }')
        """


if __name__ == '__main__':
    Channel = threading.Thread(target = Channel)
    Channel.start()

    RunServer()
