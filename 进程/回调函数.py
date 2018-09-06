#爬取数据 例子
import requests
from multiprocessing import Pool
from urllib.request import urlopen
# ret = requests.get('http://www.baidu.com')
# print(ret)
# print(ret.__dict__)
# print(ret.status_code)

def get(url):
    ret = requests.get(url)
    if ret.status_code == 200:
        return url,ret.content.decode('utf-8')

def getop(url):
    ret = urlopen(url)
    return ret.read().decode('utf-8')


def callbak(content):
    print(len(content))

if __name__ =='__main__':
    url_list =['https://www.bilibili.com/',
               'http://www.baidu.com',
               'https://home.firefoxchina.cn',
               'https://github.com/',
               'https://www.cnblogs.com',
               ]

    p = Pool(5)
    for url in url_list:
        p.apply_async(getop,args=(url,),callback=callbak)


    p.close()
    p.join()






