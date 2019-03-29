import socket
import threading


def send():
    while True:
        data = input()
        s.sendall(data.encode())


def receive():
    while True:
        data = s.recv(1024)
        print(data.decode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50000))
t1 = threading.Thread(target=send)
print("Send created")
t2 = threading.Thread(target=receive)
print("Receive created")
t1.start()
t2.start()
