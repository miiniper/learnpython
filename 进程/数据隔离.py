from multiprocessing import Process
import os


def foo():
    global n
    n = 0
    print('pid', os.getpid(), n)


if __name__ == '__main__':
    p = Process(target=foo)
    p.start()
    n = 100
    p.join()
    print(n)

