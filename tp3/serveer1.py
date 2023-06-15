import socket
import os 
from _thread import *
ServerSideSocket = socket.socket()
host ='127.0.0.1'
port = 2001
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
Server