from socket import *

udp_server = socket(AF_INET, SOCK_DGRAM)
udp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
udp_server.bind(('127.0.0.1', 9999))
print('start running.......')

while True:
    qq_msg, addr = udp_server.recvfrom(1024)
    print('来自[%s:%s]的一条消息:\033[44m%s\033[0m' % (addr[0], addr[1], qq_msg.decode('utf-8')))
    back_msg = input('回复消息：>>').strip()
    udp_server.sendto(back_msg.encode('utf-8'), addr)
udp_server.close()
