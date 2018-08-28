import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
       #print(self.request.recv(1024).decode('utf-8'))
        while True:
            ret = self.request.recv(1024).decode('utf-8')
            print(ret)
            mess = input('>>').strip()
            self.request.send(mess.encode('utf-8'))


if __name__ =='__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9998),Myserver)

    server.serve_forever()






