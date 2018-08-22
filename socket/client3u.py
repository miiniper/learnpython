from socket import *

udp_client = socket(AF_INET, SOCK_DGRAM)
while True:
    msg = input('>>').strip()
    udp_client.sendto(msg.encode('utf-8'), ('127.0.0.1', 9999))
    res, server_addr = udp_client.recvfrom(1024)
    print('返回的结果是：%s' % res.decode('utf-8'))
udp_client.close()



