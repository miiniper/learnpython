import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',9999))

while True:
    msg = input('>>').strip()
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print('server back res服务端返回结果:>>%s'%data.decode('utf-8'))

phone.close()













