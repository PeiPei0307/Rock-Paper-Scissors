import socket, time, threading, json

class Client:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.recvdata = {"Stage":"WaitP2", "P2Stage": "None"}
        self.data = {"Role":"Client", "GameStage":"WaitP2"}
    
    def connect(self, cause_error=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.address, self.port,))
        if cause_error:
            return

        recv = threading.Thread(target = self.recv_data, args = (sock,))
        recv.start()

        while True:
            time.sleep(1)
            data = json.dumps(self.data)
            sock.sendall(data.encode('utf-8'))

    def recv_data(self, sock):
        while True:
            self.recvdata = self.recv_until(sock, b'}')
            self.recvdata = json.loads(self.recvdata)
            print(self.recvdata)

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
