import socket

sk =socket.socket()
sk.connect(('127.0.0.1',9999))
ret  = sk.recv(1024).decode('utf-8')
print(ret)
msg=input('>>').strip().encode('utf-8')
sk.send(msg)
sk.close()


