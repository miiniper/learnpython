# import random

# # 1.随机小数
# print(random.random())
# print(random.uniform(1, 3))
#
# # 2.随机整数
# print(random.randint(1, 5))
# print(random.randrange(1, 5, 2))
#
# # 3.随机选择一个返回
# print(random.choice([1, '23', [4, 5]]))

# # 5.打乱列表顺序
# item = [1,2,5,8,4,3]
# random.shuffle(item)
# print(item)

# l=[]
# for i in range(5):
#     l.append(str(random.randint(0,9)))
#
# print(''.join(l))
# print(l)
#
# print(random.randint(1000,9999))


# chr(65-90)#a-z
# chr(97-122)#A-Z

# num_list = list(range(10))
# new_num_l=list(map(str,num_list))
# l =[]
# for i in range(65,93):
#     zifu=chr(i)
#     l.append(zifu)
#
# new_num_l.extend(l)
# print(new_num_l)
# ret_l=[]
# for i in range(4):
#     ret_l.append(random.choice(new_num_l))
# print(''.join(ret_l))
#

# def myrandom():
#     new_num_l=list(map(str,range(10)))
#     l = [chr(i) for i in range(65,93)]
#     new_num_l.extend(l)
#     ret_l=[random.choice(new_num_l) for i in range(4)]
#     return ''.join(ret_l)
# print(myrandom())
#
# print(chr(78))
#
#
# import os
#
# os.getcwd()  # 获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir("dirname")  # 改变当前脚本工作目录；相当于shell下cd
# os.curdir  # 返回当前目录: ('.')
# os.pardir  # 获取当前目录的父目录字符串名：('..')
# os.makedirs('dirname1/dirname2')  # 可生成多层递归目录
# os.removedirs('dirname1')  # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
# os.mkdir('dirname')  # 生成单级目录；相当于shell中mkdir dirname
# os.rmdir('dirname')  # 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
# os.listdir('dirname')  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
# os.remove()  # 删除一个文件
# os.rename("oldname", "newname")  # 重命名文件/目录
# os.stat('path/filename')  # 获取文件/目录信息
# os.sep  # 输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
# os.linesep  # 输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
# os.pathsep  # 输出用于分割文件路径的字符串 win下为;,Linux下为:
# os.name  # 输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
# os.system("bash command")  # 运行shell命令，直接显示
# os.popen("bash command)  #运行shell命令，获取执行结果
# os.environ  # 获取系统环境变量
#
#
# os.path
# os.path.abspath(
#     path)  # 返回path规范化的绝对路径 os.path.split(path) 将path分割成目录和文件名二元组返回 os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素 os.path.basename(path) 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。
# 24  # 即os.path.split(path)的第二个元素
# os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
# os.path.isabs(path)  # 如果path是绝对路径，返回True
# os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  # 将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  # 返回path所指向的文件或者目录的最后访问时间
# os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
# os.path.getsize(path)  # 返回path的大小

#
# import sys
# #print(sys.argv)
#
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
#
# name = sys.argv[1]
# password = sys.argv[2]
# if name == 'han' and password == 'han':
#     print('ok')
# else:
#     exit()
#
# sys.exit()
# print(sys.version)
# print(sys.maxsize)
# print(sys.path)
# print(sys.platform)
#


# import json
#
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# print(type(dic))
# print(dic)
# str_dic = json.dumps(dic)   #将字典转化为字符串
# print(str_dic,type(str_dic))
#
# dic2 = json.loads(str_dic)   #字符串转为字典
# print(dic2,type(dic2))
#
# list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2','k3':'v3'}]
# str_dic = json.dumps(list_dic)
# print(str_dic,type(str_dic))
#
# list_dic2 = json.loads(str_dic)
# print(str_dic,type(list_dic2))

#
# import json
# f = open('filename','w')
# dic = {'k1':'v1','k2':'v2'}
# json.dump(dic,f)   #dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
# f.close()
#
# f = open('filename')
# dic2 = json.load(f)  #load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
# f.close()
# print(type(dic2),dic2)
#

# import hashlib
# #md5_obj = hashlib.md5()
# md5_obj = hashlib.md5('hanlei'.encode('utf-8'))
# md5_obj.update('123456'.encode('utf-8'))
# print(md5_obj.hexdigest())
# md5_obj.update('hello'.encode('utf-8'))
# print(md5_obj.hexdigest())
#
#
# user = 'hanlei'
# password  = 'han'
# md5_obj = hashlib.md5(user.encode('utf-8'))
# md5_obj.update(password.encode('utf-8'))
# print(md5_obj.hexdigest())
#

# import hashlib
#
# md5_obj = hashlib.md5()
# import os
#
# filesize = os.path.getatime('filename')
# f = open('filename', 'rb')
# while filesize > 0:
#     if filesize > 1024:
#         content = f.read(1024)
#         filesize -= 1024
#     else:
#         content = f.read(int(filesize))
#         filesize -= filesize
#     md5_obj.update(content)
#
# print(md5_obj.hexdigest())
#
# import configparser
# config = configparser.ConfigParser()
# config.read('test')
# sections = config.sections()
# print(sections)
# options = config.options('mysql')
# print(options)
# items = config.items('mysql')
# print(items)
# value  = config.get('mysql','host')
# print(value,type(value))
#
#
# import configparser
# config = configparser.ConfigParser()
# config['default'] = {'serveraliveinterval':'45',
#                      'compression':'yes',
#                      'compressionlevel':'9',
#                       'forward':'yes'}
# config['bitbuch et.org'] = {'uesr':'hg'}
# config['topsecret.server.com'] = {'host port ':'10000','forward':'no'}
# with open('test','w') as configfile:
# #     config.write(configfile)
#
# import configparser
#
# config = configparser.ConfigParser()
# config.read('test')
# config.add_section('yuan')
# config.remove_section('topsecret.server.com')
# config.remove_option('default','default')
#
# config.set('yuan','y2','222222')
# config.write(open('test2','w'))






































