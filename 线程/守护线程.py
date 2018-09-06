
import time
from threading import Thread

def fun1():
    while True:
        print('*******')
        time.sleep(0.5)

def fun2():
    print('im fun2 ')
    time.sleep(5)


t = Thread(target=fun1)
t.daemon = True
t.start()

t2 = Thread(target=fun2)
t2.start()
t2.join()


