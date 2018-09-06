# 递归锁
# #会产生死锁
# from threading import Thread
# from threading import Lock
# import time
#
# noodle_lock = Lock()
# fork_lock = Lock()
# def eat1(name):
#     noodle_lock.acquire()
#     print('%s get noodles' %name)
#     fork_lock.acquire()
#     print('%s get fork ' %name)
#     print('%s eating......' %name)
#     noodle_lock.release()
#     fork_lock.release()
#
# def eat2(name):
#     fork_lock.acquire()
#     print('%s get noodles' %name)
#     time.sleep(0.5)
#     noodle_lock.acquire()
#     print('%s get fork ' %name)
#     print('%s eating......' %name)
#     fork_lock.release()
#     noodle_lock.release()
#
#
# Thread(target=eat1,args=('tttt',)).start()
# Thread(target=eat2,args=('hhhh',)).start()
# Thread(target=eat1,args=('gggg',)).start()
# Thread(target=eat2,args=('llll',)).start()
#


# 采用递归锁
from threading import Thread
from threading import RLock
import time

fork_lock = noodle_lock = RLock()


def eat1(name):
    noodle_lock.acquire()
    print('%s get noodles' % name)
    fork_lock.acquire()
    print('%s get fork ' % name)
    print('%s eating......' % name)
    noodle_lock.release()
    fork_lock.release()


def eat2(name):
    fork_lock.acquire()
    print('%s get noodles' % name)
    time.sleep(0.5)
    noodle_lock.acquire()
    print('%s get fork ' % name)
    print('%s eating......' % name)
    fork_lock.release()
    noodle_lock.release()


Thread(target=eat1, args=('tttt',)).start()
Thread(target=eat2, args=('hhhh',)).start()
Thread(target=eat1, args=('gggg',)).start()
Thread(target=eat2, args=('llll',)).start()
