import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.connect(('127.0.0.1', 9999))
while True:
    cmd = input('>>').strip()
    if not cmd: continue
    phone.send(cmd.encode('utf-8'))
    data = phone.recv(10240)
    print('返回的%s' % data.decode('gbk'))
phone.close()
