#! /usr/bin/python
# coding=UTF-8
# version:python3.x
# author: monsoon

import socket

socket.setdefaulttimeout(0.5)

def tcp_port_info(ip,port,cmd):
    try:
        # print("%s:%d -> %s " % (ip, port,cmd))
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        client.send(cmd)
        data = client.recv(1024)
        if data:
            print("%s:%d -> %s " % (ip,port,data))
    except:
        pass
    finally:
        client.close()



if __name__ == '__main__':
    for i in range(65536):
        tcp_port_info("127.0.0.1",i,"get")