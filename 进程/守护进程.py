#守护进程跟随主进程代码结束

from multiprocessing import Process
import time

def foo():
    while True:
        time.sleep(0.5)
        print('ok')



if __name__ =='__main__':
    p = Process(target=foo)
    p.daemon =True
    p.start()
    i = 0
    while i < 3:
        print('mmmmmmmmmmmmmmmmmmmmm')
        time.sleep(3)
        i += 1


#p.is_alive()   是否存活
#p.terminate()  结束进程











