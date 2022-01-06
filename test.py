import os, time, socket, threading

from server import Server
from client import Client
a = 999

def function3():
    global a
    a += 1
    print(a)

if __name__ == '__main__': 
