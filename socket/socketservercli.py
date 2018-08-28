import socket

sk = socket.socket()

sk.connect(('127.0.0.1',9998))
while True:
    mess = input('>>').strip()
    if mess == 'q':break
    sk.send(mess.encode('utf-8'))

    print(sk.recv(1024).decode('utf-8'))


sk.close()







