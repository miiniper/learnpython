import os
import hmac
import socket

secret_key = b'egge'
sk = socket.socket()
sk.bind(('127.0.0.1',9999))
sk.listen()

def check_conn(conn):
    msg = os.urandom(32)
    conn.send(msg)
    h = hmac.new(secret_key,msg)
    digest = h.digest()
    client_digest = conn.recv(1024)
    return hmac.compare_digest(digest,client_digest)


conn,addr = sk.accept()
res = check_conn(conn)
if res :
    print('ok')
    conn.close()
else:
    print('no')
    conn.close()

sk.close()







