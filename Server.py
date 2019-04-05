import socket
import threading


def send_to_all(data):
    for i in range(len(conn_list)):
        conn_list[i].send(data)


def send_and_receive(i):
    while True:
        data = conn_list[i].recv(1024)
        # print(data.decode())
        if not data:
            print("dead")
            break
        send_to_all(data)


conn_list = []
PORT = 50000
localPort = 50001
while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', PORT))
    s.listen()
    conn, addr = s.accept()
    conn.send(str(localPort).encode())
    s.close()
    conn.close()
    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ls.bind(('localhost', localPort))
    ls.listen()
    conn, addr = ls.accept()
    localPort += 1

    conn_list.append(conn)
    print("Connected: ", addr)
    t1 = threading.Thread(target=send_and_receive, args=(len(conn_list) - 1,))
    t1.start()
