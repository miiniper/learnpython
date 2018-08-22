import socket
import struct

phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',9999))
while True:
    cmd = input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    header_struct = phone.recv(4)
    unpack_res = struct.unpack('i',header_struct)
    total_size =unpack_res[0]
    recv_size= 0
    total_data=b''
    while recv_size < total_size:
        recv_data = phone.recv(1024)
        recv_size+=len(recv_data)
        total_data+=recv_data
    print('返回的消息：%s' % total_data.decode('gbk'))
phone.close()





