#!/usr/bin/python

'''
Author: Nicolas Mello Franca
Function: Simple UDP client
Date: 09/09/2017
'''

import socket

host = "192.168.1.7"

port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

c = 0

while c < 100:

	print "[*] Enviando..."

	client.sendto("AAABBBCCC", (host, port))

	data = client.recvfrom(4096)

	print data

	c += 1

client.close()
