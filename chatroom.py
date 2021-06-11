import socket
import threading

def bbs(conn):
    global user_list

    user_list.append(conn)
    try:
        while 1:
            msg = conn.recv(1024)
            if msg:
                for user in user_list:
                    user.send(msg)
    except ConnectionResetError:
        conn.close()


user_list = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('112.74.47.105', 9999))
server.listen()
while 1:
    conn, addr = server.accept()
    t = threading.Thread(target=bbs, args=(conn,))
    t.start()
