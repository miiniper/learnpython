
from socket import socket
from threading import Thread


def foo(conn):
    conn.send(b'hello')
    while True:
        #conn.send(b'hello')
        a = conn.recv(1024)
        print(a)
        conn.close()


sk = socket()
sk.bind(('127.0.0.1',9999))
sk.listen()


while True:
    conn, addr = sk.accept()
    t = Thread(target=foo,args=(conn,))
    t.start()

sk.close()




