
# coding=UTF-8

#A Simple echo Server

import socket


backlog = 5
size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5555))
s.listen(backlog)

while True:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        client.send(data)
        print(data)
    client.close()
