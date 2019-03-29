import socket
import threading


def send_and_receive():
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if not data:
            s.close()
            break
        conn.send(data)

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 50000))
    s.listen()
    conn, addr = s.accept()
    print("Connected: ", addr)
    t1 = threading.Thread(target=send_and_receive)
    t1.start()
