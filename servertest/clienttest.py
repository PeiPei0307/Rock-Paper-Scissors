import argparse, random, socket, zen_utils, time, threading

global recvdata

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    aphorisms = list(zen_utils.aphorisms)
    if cause_error:
        sock.sendall(aphorisms[0][:-1])
        return
    i = 0
    while True:
        time.sleep(0.5)
        i += 1
        print("while round = ", i)

        test = random.randint(1,3)
        if test == 1:
            text = 'testdata1'
            sock.sendall(text.encode("ascii"))
        if test == 2:
            text = 'testdata2'
            sock.sendall(text.encode("ascii"))
        if test == 3:
            text = 'testdata3'
            sock.sendall(text.encode("ascii"))
        
        global recvdata
        recvdata = zen_utils.recv_until(sock, b'.')

def printdata():
    global recvdata
    recvdata = 0
    i = 0
    while True:
        if recvdata:
            i += 1
            print("Print test : ", i)
            print('The server said', recvdata)
            recvdata = None
    """
    for aphorism in random.sample(aphorisms, 3):
        sock.sendall(aphorism)
        print(aphorism, zen_utils.recv_until(sock, b'.'))
    """
    sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()

    pd = threading.Thread(target = printdata)
    pd.start()

    address = (args.host, args.p)
    client(address, args.e)
