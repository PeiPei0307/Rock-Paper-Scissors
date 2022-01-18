import argparse, socket, zen_utils, time, threading

class Client:
    def __init__(self):
        self.recvdata = None
    
    def Connect(self, address, cause_error=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(address)
        aphorisms = list(zen_utils.aphorisms)
        if cause_error:
            sock.sendall(aphorisms[0][:-1])
            return
        i = 0

        while True:
            time.sleep(1)

            i += 1
            print("Send While round : ", i)

            sock.sendall(b'{"Datatype":"Gamestate", "State":"Waitingpunch" }')
            self.recvdata = zen_utils.recv_until(sock, b'}')

    def Printdata(self):
        while True:
            if self.recvdata:
                print('Server recv : ', self.recvdata)
                self.recvdata = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()

    client = Client()

    pd = threading.Thread(target = client.Printdata)
    pd.start()

    address = (args.host, args.p)
    client.Connect(address, args.e)
