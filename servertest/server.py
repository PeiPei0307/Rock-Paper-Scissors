import asyncio, random, threading, time

global clientlist
Clientlist = []

class GameServer(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info('peername')
        self.data = b''
        print('Accepted connection from {}'.format(self.address))

        Clientlist.append({"transport":self.transport, "address":self.address})

    def data_received(self, data):

        print(data, self.address)

        test = random.randint(1,3)
        if data == b'{"Datatype":"Gamestate", "State":"Waitingpunch" }':
            if test == 1:
                self.transport.write(b'{"Datatype":"gamestate", }')
            if test == 2:
                self.transport.write(b'{"Datatype":"gamestate", }')
            if test == 3:
                self.transport.write(b'{"Datatype":"gamestate", }')

    def connection_lost(self, exc):
        if exc:
            print('Client {} error: {}'.format(self.address, exc))
            Clientlist.remove({"transport":self.transport, "address":self.address})

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

def Channel():
    while True:
        time.sleep(1)
        if Clientlist:
            for client in Clientlist:
                print("In channel : ", client["address"])
                client["transport"].write(b'{"Datatype":"Channel", }')


if __name__ == '__main__':
    server = threading.Thread(target = Channel)
    server.start()

    RunServer()
