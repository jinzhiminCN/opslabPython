#! /usr/bin/python
# coding=UTF-8
# version:python3.x

import socket
from multiprocessing.dummy import Pool as ThreadPool


def __TCP_connect(ip, port_number, delay, output):
    # Initilize the TCP socket object
    TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    TCP_sock.settimeout(delay)

    try:
        result = TCP_sock.connect_ex((ip, int(port_number)))

        if result == 0:
            output[port_number] = 'OPEN'
        else:
            output[port_number] = 'CLOSE'

        TCP_sock.close()

    except socket.error as e:

        output[port_number] = 'CLOSE'
        pass


def scan_port(port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect_ex(('127.0.0.1', port))
        client.send(bytes("GET", encoding="utf-8"))
        data = client.recv(1024)
        print("%s:%d ->GET << %s" % ("127.0.0.1", port, data.decode('utf-8')))
        client.close()
    except Exception as e:
        pass


if __name__ == '__main__':
    # socket.setdefaulttimeout(10)
    # pool = ThreadPool(processes=100)
    # results = pool.map(scan_port, range(1000))
    # pool.close()
    # pool.join()
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect_ex(('127.0.0.1', 80))
        client.send(bytes("GET", encoding="utf-8"))
        data = client.recv(1024)
        print("%s:%d ->GET << %s" % ("127.0.0.1", 80, data.decode('utf-8')))
        client.close()
    except Exception as e:
        print(e)
