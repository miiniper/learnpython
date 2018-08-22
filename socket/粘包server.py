import socket
import subprocess
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 9999))
phone.listen(5)
print('start running........')

while True:
    conn, addr = phone.accept()
    print(conn, addr)
    while True:
        cmd = conn.recv(1024)
        print('cmd is %s' % cmd.decode('utf-8'))
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        stdout = res.stdout.read()
        stderr = res.stdout.read()
        header = struct.pack('i', len(stdout) + len(stderr))
        conn.send(header)
        conn.send(stdout)
        conn.send(stderr)
    conn.close()

phone.close()
