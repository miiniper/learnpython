import socket
import subprocess

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.bind(('127.0.0.1', 9999))
phone.listen(5)
print('starting..........')

while True:
    conn, addr = phone.accept()
    print(conn,addr)
    while True:
        cmd = conn.recv(10240)
        print('接受的是%s' % cmd.decode('utf-8'))
        res = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

        stdout = res.stdout.read()
        stderr = res.stderr.read()
        conn.send(stdout + stderr)
    conn.close()

phone.close()
