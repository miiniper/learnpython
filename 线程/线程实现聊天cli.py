from socket import socket

sk = socket()
sk.connect(('127.0.0.1',9999))


data = sk.recv(1024)
print(data)
msg= input('>>').strip()
sk.send(msg.encode('utf-8'))
sk.close()



