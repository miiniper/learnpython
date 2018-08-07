
#
# while True:
#     pnum = input('输入手机号码：')
#     if len(pnum) == 11 and pnum.isdigit() \
#         and (pnum.startswith('13') \
#         or pnum.startswith('14') \
#         or pnum.startswith('15') \
#         or pnum.startswith('17')):
#         print('is true')
#     else:
#         print('false')

#加入正则

import re
#
# pnum = input('input you number :\n')
#
# if re.match('^(13|14|15|17|18)[0-9]{9}$',pnum):
#     print('true')
# else:
#     print('false')
#
#
# ret = re.findall('s','aha sdf wesg')
# print(ret)
#
#
# ret = re.search('s','few gei ghnsoerj rhn jpg')
# print(ret.group())
#
# print(re.match('a','abc').group())
# print(re.split('[b]', 'abcd'))   #以b分割abcd
#
# print(re.sub('\d','H','cdcvr3ve6gvasdgre',1))  #替换数字替换为H，1表示替换1次
# print(re.subn('\d','H','vrev4363fdbdfb'))
#

# obj = re.compile('\d{4}')
# print(obj)
# ret = obj.search('abc4565ssgfeeee')
# print(ret.group())
# #
#
# ret = re.finditer('\d','dsf546sfsc')#finditer返回的是一个存放匹配结果的迭代器
#  # print(ret)#<callable_iterator object at 0x00000000021E9E80>
#
# print([i.group() for i in ret] )#查看剩余的左右结果
#


# from  collections import namedtuple
# point = namedtuple('point',['x','y'])
# p = point(1,2)
# print(p.x,p.y)
#
# d = {'a':'avdv','b':'bhuihweg','c':'cdfryrtsd'}
# print(d.keys())
# from collections import defaultdict
# values = [11,22,33,45,66,77,88,99]
# my_dict = defaultdict(list)
# for v in values:
#     if v > 66:
#         my_dict['k1'].append(v)
#     else:
#         my_dict['k2'].append(v)
#
# print(my_dict)
#
#
#
# from collections import Counter
# c = Counter('vqervvvv')
# print(c)
#


import time
#
# print(time.time())      #时间戳
# print(time.localtime())    #结构化时间对象
# s= time.localtime()
# print(s.tm_year)            #取值
# s2 = time.gmtime()         #tm_hour不同
# print(s2)


# print(time.localtime(1533538424))
# print(time.mktime(time.localtime()))
# print(time.strftime('%Y-%m-%d',time.localtime()))
# print(time.strftime('%y/%m/%d  %H:%M:%S'))
# print(time.strptime('2008-03-12',"%Y-%m-%d"))

#
# print(time.asctime(time.localtime(150000)))
# print(time.asctime(time.localtime()))
# print(time.ctime())
# print(time.ctime(150000))
#




















