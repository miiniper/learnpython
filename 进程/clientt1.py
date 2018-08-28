from socket import *

c = socket(AF_INET, SOCK_STREAM)
c.connect(('127.0.0.1', 9999))
while True:
    cmd = input('>>:').strip()
    if not cmd: continue
    c.send(cmd.encode('utf-8'))
    data = c.recv(1024)
    print(data.decode('utf-8'))
c.close()
