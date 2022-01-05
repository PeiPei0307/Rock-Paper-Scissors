import socket, os, threading

class Client(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.host = '127.0.0.1'
        self.port = 5000

    def run(self):
        #host, port = input("Input server address!").split(' ')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.host, int(self.port)))
        print('Client has been assigned socket name', sock.getsockname())
        print('socket closed')
        sock.close()

    def stop(self):
        self.sock.close()
        os._exit(0)