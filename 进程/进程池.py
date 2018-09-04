#效率，
#进程内存空间
#寄存器，堆栈，文件
#调度

from multiprocessing import Pool

def func(n):
    n = n - 1
    print(n)

if __name__ =="__main__":
    p = Pool(5)
    p.map(func,range(2,20))     #可迭代












