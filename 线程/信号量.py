from threading import Thread
from threading import Semaphore
import time

def func(sem,a):
    sem.acquire()
    time.sleep(1)
    print(a)
    sem.release()

sem = Semaphore(4)
for i in range(1,20):
    t = Thread(target=func,args=(sem,i))
    t.start()







