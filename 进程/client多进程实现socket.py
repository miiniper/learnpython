from socket import socket


sk = socket()
sk.connect(('127.0.0.1',9990))
msg = sk.recv(1024)
sk.send('hi'.encode('utf-8'))
print(msg)








