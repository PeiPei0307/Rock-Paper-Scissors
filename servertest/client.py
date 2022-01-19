import argparse, socket, time, threading, json

class Client:
    def __init__(self):
        self.recvdata = None
        self.control = False
    
    def connect(self, address, cause_error=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        if cause_error:
            return

        recv = threading.Thread(target = self.recv_data, args = (sock,))
        recv.start()

        printdata = threading.Thread(target = self.printdata)
        printdata.start()

        while True:
            time.sleep(1)
            if self.control == False:
                sock.sendall(b'''{"Role":"Client", "State":"Waitingpunch"}''')
            else:
                sock.sendall(b'''{"Role":"Client", "State":"Rock"}''')

    def recv_data(self, sock):
        while True:
            self.recvdata = self.recv_until(sock, b'}')
            data = json.loads(self.recvdata)
            if data["Stage"] != "Result":
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()

    client = Client()

    address = (args.host, args.p)
    client.connect(address, args.e)
