
# coding=UTF-8

# A Simple echo Server

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 12345))
s.listen(5)

while True:
    client, address = s.accept()
    data = client.recv(1024)
    if data:
        client.send(data)
        print(data)
    client.close()
