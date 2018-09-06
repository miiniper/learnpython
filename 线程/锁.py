import time
from threading import Thread
from threading import Lock
#
# def fun():
#     global n
#     tmp=n
#     time.sleep(0.1)
#     n = tmp -1
#
# n= 10
# l= []
# for i in range(10):
#     t = Thread(target=fun)
#     t.start()
#     l.append(t)
#
# for t in l:t.join()
#
# print(n)





def fun(lock):
    global n
    lock.acquire()
    tmp=n
    time.sleep(0.1)
    n = tmp -1
    lock.release()

n= 10
l= []
lock = Lock()
for i in range(10):
    t = Thread(target=fun,args=(lock,))
    t.start()
    l.append(t)

for t in l:t.join()

print(n)


