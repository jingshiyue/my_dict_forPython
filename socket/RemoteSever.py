#-*- coding: utf-8 -*-

import socket
import os
import threading

import urllib.parse
import ctypes
import datetime


local_ip = '0.0.0.0'        # 配置socket server绑定的本地IP
local_port = 4321           # 配置socket server绑定的本地端口

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((local_ip, local_port))
server.listen(5)

# 只响应白名单中的计算机发来的任务
# admin_filter的key()
admin_filter = {}
admin_filter['175.168.1.107'] = {'exe'}
admin_filter['175.168.1.107'] = {'bat'}


print('White list:' + str(admin_filter))
print('Server bind on %s:%s' % (local_ip, str(local_port)))
print('-----------------Server starting success-----------------')


def exe_prog(msg):
    # 路径由空格，加上引号就好了 -_-!!!!!
    #os.system(u"\"C:\Program Files (x86)\TTPlayer\TTPlayer.exe\"".encode("gbk"))
    os.system(msg)
    # os.system("C:\ProgramData\Anaconda3\envs\py2\python.exe F:\\source_files\\quant\\remote_pc_control\\exe_calc.py")

while 1:
    conn, addr = server.accept()
    msg = urllib.parse.unquote(conn.recv(1024).decode('utf-8'))
    
    peer_name = conn.getpeername()
    sock_name = conn.getsockname()

    # peer_name是个tuple，peer_name[0]是ip，peer_name[1]是端口号
    now_dt = str(datetime.datetime.now())
    print(u'%s, visitor: %s:%s'%(now_dt, peer_name[0],peer_name[1])) # , sock_name
    # 所谓的白名单，管理员权限验证
    if peer_name[0] in admin_filter.keys():
        print(msg)
        if '"quit"' == msg: # 可能是 'quit' 可能是 '"quit"' …… 自己检验一下
            conn.close()
            exit(0)
        t = threading.Thread(target=exe_prog,args=(msg,))
        print(t.getName)
        t.start()

    #conn.send('server: I received '+msg)