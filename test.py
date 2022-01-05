import os, time, socket, threading

'''
class ServerThread(threading.Thread):

    def __init__(self, host, port):
        threading.Thread.__init__(self)
        self.host = host
        self.port = port

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
            sc.close()
            print('  Reply sent, socket closed')

    def stop(self):
        self.sock.close()
        os._exit(0)

    

if __name__ == '__main__': 
    server = ServerThread('127.0.0.1', 5000)
    server.start()
    time.sleep(1)
    server.stop()
'''

from server import Server
from client import Client
a = 999

def function3():
    global a
    a += 1
    print(a)

if __name__ == '__main__': 
