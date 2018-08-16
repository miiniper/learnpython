
#server
import socket

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
phone.bind(('127.0.0.1',9999))

print('starting......')
phone.listen(5)
while True:
    coon,client_addr=phone.accept()
    print(coon,client_addr)
    while True:
        try:
            data = coon.recv(1024)
            print('client data 收到消息:%s'%data.decode('utf-8'))
            coon.send(data.upper())
        except Exception:
            break
    coon.close()
phone.close()















