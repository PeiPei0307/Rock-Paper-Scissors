import socket

def Client():
    host = '127.0.0.1'
    port = 5000
    #host, port = input("Input server address!").split(' ')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))
    print('Client has been assigned socket name', sock.getsockname())
    sock.close()

if __name__ == '__main__':
    Client()