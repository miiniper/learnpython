from socket import socket
from multiprocessing import Process

def foo(conn):
    conn.send('hello'.encode('utf-8'))
    res = conn.recv(1024).decode('utf-8')
    print(res)
    conn.close()


if __name__ == '__main__':
    sk = socket()
    sk.bind(('127.0.0.1',9990))
    sk.listen()

    while True:
        conn,addr = sk.accept()
        p = Process(target=foo,args=(conn,))
        p.start()
    sk.close()



