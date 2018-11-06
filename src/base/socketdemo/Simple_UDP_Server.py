
# coding=UTF-8
#@descript:一个简单的UDP服务端程序
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 4444))

while True:
    try:
        message, addr = s.recvfrom(1024 * 4)
        print("Get data from ", message, addr)
        s.sendto(message, addr)
    except Exception as err:
        print(err)
        continue
