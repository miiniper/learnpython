from socket import *

udp_client = socket(AF_INET,SOCK_DGRAM)


while True:
    mess = input('>>').strip()
    udp_client.sendto(mess.encode('utf-8'),('127.0.0.1',9999))
    back_msg , addr = udp_client.recvfrom(1024)
    print('来自[%s:%s]的一条消息:\033[41m%s\033[0m'%(addr[0],addr[1],back_msg.decode('utf-8')))
udp_client.close()


