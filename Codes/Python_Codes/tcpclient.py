#!/usr/bin/python

import socket
import sys

try:

    ip = sys.argv[1]
    port = 80

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    my_socket.connect((ip, port))

    my_socket.send('GET / HTTP/1.1\r\n\r\n')

    r = my_socket.recv(1024)

    print r

except Exception as erro:

    print erro
    my_socket.close()
