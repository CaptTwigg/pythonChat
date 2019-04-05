import socket
import threading


def send_to_all(data):
    for i in range(len(conn_list)):
        conn_list[i].send(data)


def send_and_receive(x):
    while True:
        data = conn_list[x].recv(1024)
        # print(data.decode())
        if not data:
            print("dead")
            break
        file = open("chat.txt", "a+")
        file.write(data.decode() + "\n")
        file.close()
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
    # user_name = conn.recv(1024).decode()
    s.close()
    conn.close()

    ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ls.bind(('localhost', localPort))
    ls.listen()
    conn, addr = ls.accept()
    localPort += 1
    f = open("chat.txt", "r")
    for i in f:
        conn.send(i.encode())
    f.close()
    conn_list.append(conn)
    print("Connected: ", addr)
    t1 = threading.Thread(target=send_and_receive, args=(conn_list.index(conn),))
    t1.start()
