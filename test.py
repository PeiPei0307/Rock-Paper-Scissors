import argparse, socket, threading, time

'''
def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        data += more
        if not more:
            return 
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
            
    return data
'''

def server_thread(sc, count):
    while True:
        data = sc.recv(1024)
        print('  Client at ',  sc.getpeername(), ' message:', repr(data) ,)
        message = 'Your data was {} bytes long'.format(len(data))
        sc.sendall(message.encode('utf-8'))
        if data == b"|exit|":
            break
    sc.close()
    print('  Reply sent, socket closed')

def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    while True:
        print('Listening at', sock.getsockname())
        print('Waiting to accept a new connection')
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sc.getsockname())
        print('  Socket peer:', sc.getpeername())
        sc = threading.Thread(target = server_thread, args = (sc, 6))
        sc.start()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    while True:
        message = input(">>>")
        sock.sendall(message.encode('utf-8'))
        reply = sock.recv(1024)
        print('The server said', repr(reply))
        if message == "|exit|":
            break
    sock.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)