
# coding=UTF-8
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("hello", ('127.0.0.1', 4444))
buf = s.recvfrom(2048)
print(buf)
