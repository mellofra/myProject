#! usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.109", 21))
r = s.recv(1024)
print r
s.send("USER test\r\n")
r = s.recv(1024)
print r
s.send("PASS testzrzn")
r = s.recv(1024)
print r