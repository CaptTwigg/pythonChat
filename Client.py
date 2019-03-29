import socket
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    s.send("hello from client".encode())

    data = s.recv(1024)
    print(data.decode())
