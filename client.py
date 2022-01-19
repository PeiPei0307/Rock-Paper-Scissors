import socket, time, threading, json

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.recvdata = None
        self.data = {"Role":"Client", "State":"Waitingpunch"}
    
    def connect(self, cause_error=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.address, self.port,))
        if cause_error:
            return

        recv = threading.Thread(target = self.recv_data, args = (sock,))
        recv.start()

        printdata = threading.Thread(target = self.printdata)
        printdata.start()

        while True:
            time.sleep(1)
            data = json.dumps(self.data)
            if self.data["State"] == "Waitingpunch":
                sock.sendall(data.encode('utf-8'))
            else:
                sock.sendall(data.encode('utf-8'))

    def recv_data(self, sock):
        while True:
            self.recvdata = self.recv_until(sock, b'}')
            data = json.loads(self.recvdata)
            if data["State"] != "Result":
                pass
            else:
                self.control = False


    def printdata(self):
        while True:
            if self.recvdata:
                print('ServerRecv : ', self.recvdata)
                self.recvdata = None

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
