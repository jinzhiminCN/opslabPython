
# coding=UTF-8

import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))
client.send("hello world")
data = client.recv(1024)
if data:
    print(data)
client.close()

