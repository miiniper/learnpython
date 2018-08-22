from socket import *

udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(('127.0.0.1',9999))
while True:
    msg, client_addr = udp_server.recvfrom(1024)
    print('收到的消息是：%s'%msg.decode('utf-8'))
    udp_server.sendto(msg.upper(),client_addr)
udp_server.close()

