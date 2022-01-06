import socket, os, threading

class Server(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5000

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        print('Listening at', self.sock.getsockname())
        while True:
            print('Waiting to accept a new connection')
            sc, sockname = self.sock.accept()
            print('We have accepted a connection from', sockname)
            print('  Socket name:', sc.getsockname())
            print('  Socket peer:', sc.getpeername())
            self.talk(sc)
            
    def talk(self, sc):
        while True:
            data = sc.recv(1024)
            print('  Client at ',  sc.getpeername(), ' message:', repr(data) ,)
            message = 'Your data was {} bytes long'.format(len(data))
            sc.sendall(message.encode('utf-8'))
            if data == b"|exit|":
                break
        sc.close()
        print('  Reply sent, socket closed')

    def stop(self):
        self.sock.close()
        os._exit(0)
