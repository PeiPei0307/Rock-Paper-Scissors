import socket, time, threading, json

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.recvdata = {"Role":None, "Stage":"None", "P2Stage":None, "P1":None, "P2":None, "Punch":"None", "Ans":None}
        self.data = {"Role":"Client", "Stage":"Connect", "Punch":None}
    
    def connect(self, cause_error=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.address, self.port,))
        if cause_error:
            return

        printdata = threading.Thread(target = self.printdata)
        printdata.start()

        recv = threading.Thread(target = self.recv_data, args = (sock,))
        recv.start()

        while True:
            if self.data["Stage"] != None:
                data = json.dumps(self.data)
                sock.sendall(data.encode('utf-8'))
                self.data["Stage"] = None

    def recv_data(self, sock):
        while True:
            self.recvdata = self.recv_until(sock, b'}')
            self.recvdata = json.loads(self.recvdata)

    def printdata(self):
        while True:
            time.sleep(2)
            if self.recvdata:
                print('ServerRecv : ', self.recvdata)

    def recv_until(self, sock, suffix):
        message = sock.recv(4096)
        if not message:
            raise EOFError('socket closed')
        while not message.endswith(suffix):
            data = sock.recv(4096)
            if not data:
                raise IOError('received {!r} then socket closed'.format(message))
            message += data
        return message.decode("utf-8")
