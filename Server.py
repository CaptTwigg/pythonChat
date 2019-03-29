import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


def reciveDataSendData():
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                print("dead")
                break
            conn.sendall(data)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        try:
            conn, addr = s.accept()
            threading.Thread(target=reciveDataSendData())

        except:
            print("Can't connect")
