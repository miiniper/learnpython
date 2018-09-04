from multiprocessing import Pool
import socket

def func(conn):
    conn.send(b'hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()


if __name__== '__main__':
    p = Pool(5)
    sk = socket.socket()
    sk.bind(('127.0.0.1',9999))
    sk.listen()
    while True:
        conn,addr = sk.accept()
        p.apply_async(func , args=(conn,))
    sk.close()




