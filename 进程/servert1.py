from socket import *
from multiprocessing import Process

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('starting running.....')


def talking(conn, addr):
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()


if __name__ == '__main__':
    while True:
        conn, addr = s.accept()
        print(conn, addr)
        p = Process(target=talking, args=(conn, addr))
        p.start()
    s.close()
