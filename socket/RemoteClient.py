#-*- coding: utf-8 -*-

import socket
from urllib import parse
from time import sleep

def send_cmd(ip_list,port,instr):
    try:
        for ip in ip_list:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((ip, port))
            client.settimeout(5)
            client.sendall(parse.quote(instr).encode('utf-8'))
            print("ip：%s 连接服务器成功..." %ip)
    except Exception as e:
        print(e)
    finally:
        client.close()

msg = r"D:\socket\time.bat"

while True:
    send_cmd(['175.168.1.152','175.168.1.151'],4321,msg)
    sleep(100)